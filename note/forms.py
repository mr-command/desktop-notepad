from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Note

class AddNote(forms.ModelForm):
    title = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control',
                                      'placeholder':'Enter file name',
                                      'style':'width:360px;height:40px;margin-top:40px;margin-left:24%;',
                                      })
    )

    content = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'id':'txt',
                                     'placeholder':'Enter your content',
                                     'style':'margin-top:80px;margin-bottom:80px;outline: none; font-size: 22px;width: 1000px;height: 700px;margin-left:24%;',
                                     })
    )
    class Meta:
        model = Note
        fields = ['title','content']
