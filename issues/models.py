from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Bug(models.Model):
    """
    A Bug Report
    """
    title = models.CharField(max_length=200)
    decsription = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    fixed = models.BooleanField(blank=False, default=False)
    date_fixed = models.DateTimeField(blank=True, null=True)
    score = models.IntegerField(default=0)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
        
        

class Feature(models.Model):
    """
    A Feature Suggestion
    """
    title = models.CharField(max_length=200)
    decsription = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    added = models.BooleanField(blank=False, default=False)
    date_added = models.DateTimeField(blank=True, null=True)
    score = models.IntegerField(default=0)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title