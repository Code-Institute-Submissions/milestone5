from django import forms
from .models import Bug, Feature

class ReportBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title', 'description')
        
        
class SuggestFeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('title', 'description')