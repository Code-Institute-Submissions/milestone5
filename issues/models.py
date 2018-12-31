from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


# I DECIDED TO KEEP THE BUGS AND FEATURES SEPERATE
# THIS IS DONE THROUGHT OUT THE APP SO THAT THEY CAN BE WORKED ON INDIVIDUALLY
# HELPS KEEP THE CODE TIDY

class Bug(models.Model):
    """
    A Bug Report
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    working_on = models.BooleanField(blank=False, default=False)
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
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    working_on = models.BooleanField(blank=False, default=False)
    added = models.BooleanField(blank=False, default=False)
    date_added = models.DateTimeField(blank=True, null=True)
    score = models.IntegerField(default=0)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title