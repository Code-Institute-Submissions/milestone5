from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


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
  
  return render(request, 'login.html')