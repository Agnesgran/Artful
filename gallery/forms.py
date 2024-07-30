from django import forms
from .models import Profile, Art, Comment

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'age', 'preferred_medium', 'user_type']

class ArtUploadForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = ['title', 'description', 'price', 'image', 'art_type']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'age', 'preferred_medium', 'user_type']
