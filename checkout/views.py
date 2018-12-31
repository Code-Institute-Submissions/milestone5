from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from accounts.models import Token
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required()
def checkout(request):
  if request.method=="POST":
    order_form = OrderForm(request.POST)
    payment_form = MakePaymentForm(request.POST)
    
    
    
    if order_form.is_valid() and payment_form.is_valid():
      
      cart = request.session.get('cart', {})
      total = 0
      tokens_bought = 0
      for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        tokens_bought += product.token_amount
        
      
      try:
        customer = stripe.Charge.create(
          amount = int(total * 100),
          currency = "GBP",
          description = request.user.email,
          card = payment_form.cleaned_data['stripe_id'],
        )
      except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
       
       
      # ONCE WE ARE SURE THE CUSTOMER HAS PAID WE CAN ADD TOKENS TO THEIR ACCOUNT
      # AND RECORD THE ORDERS AGAINST THEIR USERNAME
      if customer.paid:
        messages.success(request, "You have successfully paid")
        request.session['cart'] = {}
        
        order = order_form.save(commit=False)
        order.date = timezone.now()
        order.purchased_by = request.user
        order.save()
        
        
        for id, quantity in cart.items():
          product = get_object_or_404(Product, pk=id)

          order_line_item = OrderLineItem(
              order = order,
              product = product,
              quantity = quantity
              )
          order_line_item.save()
        
        if Token.objects.filter(user=request.user).exists():
          tokens = Token.objects.get(user=request.user)

          total_tokens = int(tokens.amount) + tokens_bought
        else:
          total_tokens = tokens_bought
        
        values_to_update = {'amount':total_tokens}
      
        obj_token, created = Token.objects.update_or_create(
        user=request.user, defaults=values_to_update)
        
        return redirect(reverse('products'))
      else:
        messages.error(request, "Unable to take payment")
    else:
      print(payment_form.errors)
      messages.error(request, "We were unable to take a payment with that card!")
  else:
    payment_form = MakePaymentForm()
    order_form = OrderForm()
        
  return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE_KEY})