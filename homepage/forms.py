# encoding=utf8
from django import forms
from homepage.models import Idea, Challenge


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('title','challenge','description','email')
        widgets = {
            'title' :   forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Title of the idea",
            }),
                'challenge' :   forms.Select(attrs={
                'class': "form-control",
            }),
            'description' : forms.Textarea(attrs={
                    'class': "form-control",
                    'rows': "3",
                    'placeholder': "Short description",
            }),
            'email' :   forms.EmailInput(attrs={
                'class': "form-control",
                'placeholder': "Contact email",
            })
        }
        