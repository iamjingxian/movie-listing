from .models import Movie
from django.forms import ModelForm
from django import forms

class MovieForm(ModelForm):
    name = forms.TextInput()
    use_required_attribute = False
    class Meta:
        model = Movie
        fields = '__all__'