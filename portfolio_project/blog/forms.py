from django import forms
from django.forms import inlineformset_factory  


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search ')

