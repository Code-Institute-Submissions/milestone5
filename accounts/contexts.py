from django.shortcuts import get_object_or_404
from accounts.models import Token

def display_tokens(request):
  token_total = 0
  if request.user.is_authenticated():
    if Token.objects.filter(user=request.user):
      tokens = get_object_or_404(Token, user=request.user)
    
      token_total = tokens.amount
  return { 'token_total': token_total}