from django.shortcuts import render


def view_charts(request):
  return render(request,'charts.html')
  
  