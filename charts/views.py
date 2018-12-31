from django.shortcuts import render
from django.http import JsonResponse
from issues.models import Bug, Feature
from datetime import date
import datetime


# THESE VIEWS ARE SPECIFICALLY MADE TO RETRIEVE DATA FROM THE DATABASE AND PASS
# IT TO JAVASCRIPT OF THE FONT END USING A JSON RESPONSE. 

# THE DATA IS ONCE AGAIN ACQUIRED ASYNCHRONOUSLY
def view_charts(request):
  return render(request,'charts.html')
  

def get_data(request):
  fixed_bugs = Bug.objects.filter(fixed=True).order_by('-date_fixed')
  total_fixed_today  = fixed_bugs.filter(date_fixed__date=date.today()).count()
  
  this_month = datetime.datetime.now().month
  total_fixed_month = Bug.objects.filter(date_fixed__month=this_month).count()
  total_added_month  = Feature.objects.filter(date_added__month=this_month).count()
  
  this_year = datetime.datetime.now().year
  total_fixed_year = Bug.objects.filter(date_fixed__year=this_year).count()
  total_added_year  = Feature.objects.filter(date_added__year=this_year).count()
  
  added_features = Feature.objects.filter(added=True).order_by('-date_added')
  total_added_today  = added_features.filter(date_added__date=date.today()).count()
  
  
  
  labels = ["Bugs", "Features"]
  items = [total_fixed_today, total_added_today]
  
  itemsmonth = [total_fixed_month, total_added_month]
  
  itemsyear = [total_fixed_year, total_added_year]
  
  data = {
    "labels":labels,
    "items":items,
    "itemsmonth":itemsmonth,
    "itemsyear":itemsyear
  }
  
  return JsonResponse(data)