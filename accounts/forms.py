from django import forms

class UserLoginForm(forms.Form):
  username = forms.CharField(label="Username or Email")
  password = forms.CharField(widget=forms.PasswordInput)