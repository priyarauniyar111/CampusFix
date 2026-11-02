from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Complaint
class SignUpForm(UserCreationForm):
 email=forms.EmailField(required=True);first_name=forms.CharField(max_length=40,required=True)
 class Meta:model=User;fields=('first_name','username','email','password1','password2')
 def save(self,commit=True):
  user=super().save(commit=False);user.email=self.cleaned_data['email'];user.first_name=self.cleaned_data['first_name']
  if commit:user.save()
  return user
class ComplaintForm(forms.ModelForm):
 class Meta:
  model=Complaint;fields=['title','category','location','priority','description','image']
  widgets={'description':forms.Textarea(attrs={'rows':5,'placeholder':'Tell us what happened and how it affects you…'})}
