from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

def logout(request):
  """Log user out"""
  auth.logout(request)
  messages.success(request, "You have been logged out!")
  return redirect(reverse('tracker_home'))