from django import forms
from . models import Category, movies

class customForm(forms.Form):
    name = forms.CharField(max_length=233)
    content = forms.CharField(widget=forms.Textarea)


class movieForm(forms.ModelForm):
    class Meta:
        model = movies
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
