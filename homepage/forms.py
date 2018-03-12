# encoding=utf8
from django import forms
from homepage.models import Idea


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('description','email')