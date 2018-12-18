from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User


"""
Logs user out and returns them to the issue-tracker home page
"""
@login_required
def logout(request):
  auth.logout(request)
  messages.success(request, "You have been logged out!")
  return redirect(reverse('tracker_home'))

  

"""
Brings User to login page, if they submit valid form it
logs user in and returns them to the issue-tracker home page
""" 
def login(request):
  
  if request.user.is_authenticated:
    return redirect(reverse('tracker_home'))
  
  if request.method == "POST":
    login_form = UserLoginForm(request.POST)
    
    if login_form.is_valid():
      user = auth.authenticate(username=request.POST['username'],
                              password=request.POST['password'])
      
      
      if user:
        auth.login(user=user, request=request)
        messages.success(request, "Success, You're In!")
        return redirect(reverse('tracker_home'))
      else: login_form.add_error(None, "Oops! Either Your Username or Password is Incorrect")
    
  else:
    login_form = UserLoginForm()
  
  return render(request, 'login.html', {"login_form": login_form})
  
  
  

"""
REGISTRATION
"""
def register(request):
  if request.user.is_authenticated:
    return redirect(reverse('tracker_home'))
    
  if request.method == 'POST':
    registration_form = UserRegistrationForm(request.POST)
    
    if registration_form.is_valid():
      registration_form.save()
      
      user = auth.authenticate(username=request.POST['username'],
                              password=request.POST['password1'])
                              
      if user:
        auth.login(user=user, request=request)
        messages.success(request, "Congratulations! You're One Of Us Now.")
        return redirect(reverse('tracker_home'))
      else: messages.error(request, "Unable to register your account at this time")
                              
  else:
    registration_form = UserRegistrationForm()
  return render(request, 'register.html', {"registration_form": registration_form})
  
  
"""
USER PROFILE
"""
@login_required
def profile(request):
  user = User.objects.get(email=request.user.email)
  return render(request, 'profile.html', {"profile": user})