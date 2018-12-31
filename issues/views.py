from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse
from .models import Bug, Feature
from accounts.models import Token
from comments.models import BugComment, FeatureComment
from .forms import ReportBugForm, SuggestFeatureForm



# THIS IS THE MAIN APP FOR DEALING WITH ALL THE ISSUES
# I HAVE SPLIT THE CODE INTO BUGS AND FEATURES THIS SHOULD MAKE IT EASIER TO FOLLOW
# AND MAINTAIN IN THE FUTURE


# BUG LOGIC
def all_bugs_fixed(request):
  bugs = Bug.objects.filter(fixed=True).order_by('-date_fixed')
  total = bugs.count()
  status = "fixed"
  return render(request, "allbugs.html", {'bugs':bugs, 'total':total, 'status':status})
  
  
def all_bugs_working(request):
  bugs = Bug.objects.filter(working_on=True).order_by('-score')
  total = bugs.count()
  status = "working-on"
  return render(request, "allbugs.html", {'bugs':bugs, 'total':total, 'status':status})
  
def all_bugs_todo(request):
  bugs = Bug.objects.filter(fixed=False, working_on=False).order_by('-score')
  total = bugs.count()
  status = "todo"
  return render(request, "allbugs.html", {'bugs':bugs, 'total':total, 'status':status})
  
  
def bug_detail(request, pk):
  bug = get_object_or_404(Bug, pk=pk)
  comments = BugComment.objects.filter(bug=pk).order_by('-date_created')
  return render(request, "bugdetail.html", {'bug': bug, 'comments':comments})
  
  
@login_required  
def upvote_bug(request, pk):
  bug = get_object_or_404(Bug, pk=pk)
  bug.score += 1
  bug.save()
  
  data = {
        'score': bug.score
    }
  return JsonResponse(data)
  
  
@login_required
def bug_fixed(request, pk):
  bug = get_object_or_404(Bug, pk=pk)
  bug.fixed = True
  bug.date_fixed = timezone.now()
  bug.save()
  return redirect(bug_detail, bug.pk)


@login_required
def report_bug(request):
  if request.method == "POST":
    form = ReportBugForm(request.POST)
    if form.is_valid():
      bug = form.save(commit=False)
      bug.user = request.user
      bug.save()
      return redirect(bug_detail, bug.pk)
  else:
    form = ReportBugForm()
  return render(request, "reportbug.html", {'form': form})
  



# FEATURE LOGIC
def all_features_added(request):
  features = Feature.objects.filter(added=True).order_by('-date_added')
  total = features.count()
  status = "added"
  return render(request, "allfeatures.html", {'features':features, 'total':total, 'status':status})
  
  
def all_features_working(request):
  features = Feature.objects.filter(working_on=True).order_by('-score')
  total = features.count()
  status = "working-on"
  return render(request, "allfeatures.html", {'features':features, 'total':total, 'status':status})
  
def all_features_pending(request):
  features = Feature.objects.filter(added=False, working_on=False).order_by('-score')
  total = features.count()
  status = "pending"
  return render(request, "allfeatures.html", {'features':features, 'total':total, 'status':status})
  
  
def feature_detail(request, pk):
  feature= get_object_or_404(Feature, pk=pk)
  comments = FeatureComment.objects.filter(feature=pk).order_by('-date_created')
  return render(request, "featuredetail.html", {'feature': feature, 'comments': comments})
  

@login_required  
def upvote_feature(request, pk):
  feature = get_object_or_404(Feature, pk=pk)
  if Token.objects.filter(user=request.user).exists():
    tokens = get_object_or_404(Token, user=request.user)
    
    if tokens.amount > 0:
      feature.score += 1
      feature.save()
      
      tokens.amount -= 1
      tokens.save()
      
      data = {
        'score': feature.score,
        'tokens': tokens.amount
      }
    else:
      data = {
        'score': feature.score,
        'tokens': '0',
        'message': "You Have No Tokens To Upvote"
      }
    return JsonResponse(data) 
    
    
    
@login_required
def feature_added(request, pk):
  feature = get_object_or_404(Feature, pk=pk)
  feature.added = True
  feature.date_added = timezone.now()
  feature.save()
  return redirect(feature_detail, feature.pk)


@login_required  
def suggest_feature(request):
  if request.method == "POST":
    form = SuggestFeatureForm(request.POST)
    if form.is_valid():
      feature = form.save(commit=False)
      feature.user = request.user
      feature.save()
      return redirect(feature_detail, feature.pk)
  else:
    form = SuggestFeatureForm()
  return render(request, "suggestfeature.html", {'form': form})