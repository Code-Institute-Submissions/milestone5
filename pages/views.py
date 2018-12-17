from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def issue_tracker(request):
    return render(request, 'issuetracker.html')