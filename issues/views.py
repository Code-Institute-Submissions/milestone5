from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse
from .models import Bug, Feature
from accounts.models import Token
from .forms import ReportBugForm, SuggestFeatureForm


def all_bugs(request):
  return render(request, "allbugs.html")
  
  
def bug_detail(request, pk):
  bug = get_object_or_404(Bug, pk=pk)
  return render(request, "bugdetail.html", {'bug': bug})
  
  
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
  




def all_features(request):
  return render(request, "allfeatures.html")
  
  
def feature_detail(request, pk):
  feature= get_object_or_404(Feature, pk=pk)
  return render(request, "featuredetail.html", {'feature': feature})
  

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