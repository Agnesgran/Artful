from django import forms
from .models import Profile
from .models import Art

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'age', 'preferred_medium', 'user_type']

class ArtUploadForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = ['title', 'description', 'price', 'image', 'art_type']
