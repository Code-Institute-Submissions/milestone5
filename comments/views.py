from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BugComment, FeatureComment
from .forms import BugCommentForm, FeatureCommentForm
from issues.models import Bug, Feature
from issues.views import bug_detail, feature_detail

# AGAIN EVEN THE COMMENTS FOR EACH TYPE OF ISSUE ARE KEPT APART, THERE ARE TWO VIEWS, TWO MODELS AND TWO FORMS
# ALTHOUGH THIS MAY BE SLIGHTLY MORE WORK, IN THE LONG RUN IT WILL BE EASIER FOR ANYONE TO VIEW THE CODE 
# AND KNOW WHAT IS WHAT

@login_required
def add_bug_comment(request, pk):
  if request.method == "POST":
    form = BugCommentForm(request.POST)
    if form.is_valid():
      bug = get_object_or_404(Bug, pk=pk)
      comment = form.save(commit=False)
      comment.creator = request.user
      comment.bug = bug
      comment.save()
      return redirect(bug_detail, pk)
  else:
    form = BugCommentForm()
  return render(request, "addcomment.html", {'form': form})
  
  
@login_required
def add_feature_comment(request, pk):
  if request.method == "POST":
    form = FeatureCommentForm(request.POST)
    if form.is_valid():
      feature = get_object_or_404(Feature, pk=pk)
      comment = form.save(commit=False)
      comment.creator = request.user
      comment.feature = feature
      comment.save()
      return redirect(feature_detail, pk)
  else:
    form = FeatureCommentForm()
  return render(request, "addcomment.html", {'form': form})
