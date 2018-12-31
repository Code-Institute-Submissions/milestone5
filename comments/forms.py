from django import forms
from .models import BugComment, FeatureComment

class BugCommentForm(forms.ModelForm):
    class Meta:
        model = BugComment
        fields = ('text',)
        

class FeatureCommentForm(forms.ModelForm):
    class Meta:
        model = FeatureComment
        fields = ('text',)