from django import forms
from django.forms import ModelForm, fields
from .models import Album

class AlbumForm(ModelForm):
    image = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    class Meta:
        model = Album
        fields = ('image',)
