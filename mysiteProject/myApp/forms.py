from dataclasses import field, fields
from django import forms
from .models import PostModel

class PostForm(forms.ModelForm):
    title= forms.CharField(label = 'Title', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content= forms.CharField(label = 'content' , widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = PostModel
        exclude = ('user',)