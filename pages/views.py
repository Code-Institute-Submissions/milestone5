from django.shortcuts import render
from issues.models import Bug, Feature
from datetime import date

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
    


# HERE THE BUG AND FEATURE MODEL OBJECTS ARE FILTERED BEFORE BEING SENT TO TEMPLATE
# THIS PREVENTS TOO MUCH LOGIC HAPPENING IN THE TEMPLATE, HERE IS MUCH TIDIER
def issue_tracker(request):
    fixed_bugs = Bug.objects.filter(fixed=True).order_by('-date_fixed')
    total_fixed = fixed_bugs.count()
    
    total_fixed_today  = fixed_bugs.filter(date_fixed__date=date.today()).count()
    
    working_bugs = Bug.objects.filter(working_on=True).order_by('-score')
    total_working = working_bugs.count()
    
    other_bugs = Bug.objects.filter(working_on=False, fixed=False).order_by('-score')
    total_other = other_bugs.count()
    
    
    added_features = Feature.objects.filter(added=True).order_by('-date_added')
    total_added = added_features.count()
    
    working_features = Feature.objects.filter(working_on=True).order_by('-score')
    total_working_features = working_features.count()
    
    other_features = Feature.objects.filter(working_on=False, added=False).order_by('-score')
    total_other_features = other_features.count()
    return render(request, 'issuetracker.html', {'fixed_bugs':fixed_bugs,
                                                'total_fixed':total_fixed,
                                                'total_fixed_today':total_fixed_today,
                                                'working_bugs':working_bugs,
                                                'total_working':total_working,
                                                'other_bugs':other_bugs,
                                                'total_other':total_other,
                                                'added_features':added_features,
                                                'total_added':total_added,
                                                'working_features':working_features,
                                                'total_working_features':total_working_features,
                                                'other_features':other_features,
                                                'total_other_features':total_other_features,
                                                })
                                                
                                                
                                                
                                                
                                                
                                                
