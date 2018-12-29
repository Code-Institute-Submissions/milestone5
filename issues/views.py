from django.shortcuts import render, redirect, reverse

def report_bug(request):
  return render(request, "reportbug.html")
  
  
def suggest_feature(request):
  return render(request, "suggestfeature.html")