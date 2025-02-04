from django import forms
from .models import Work

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['work', 'un']

    work = forms.CharField(required=False)
    un = forms.CharField(required=False)