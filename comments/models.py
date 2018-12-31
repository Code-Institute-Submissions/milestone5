from django.db import models
from django.contrib.auth import get_user_model
from issues.models import Bug

class BugComment(models.Model):
    """
    Comments For Bug Reports
    """
    bug = models.ForeignKey('issues.Bug', on_delete=models.CASCADE, related_name='bugComments')
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='bugComments')
    
    def __str__(self):
        return self.title
        

class FeatureComment(models.Model):
    """
    Comments For Feature Suggestions
    """
    feature = models.ForeignKey('issues.Feature', on_delete=models.CASCADE, related_name='featureComments')
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='featureComments')
    
    def __str__(self):
        return self.title
