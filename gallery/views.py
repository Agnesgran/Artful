from django.shortcuts import render
from .models import Art

def home(request):
    return render(request, 'gallery/home.html')

def art_gallery(request):
    artworks = Art.objects.all()
    return render(request, 'gallery/art_gallery.html', {'artworks': artworks})

def profile(request):
    return render(request, 'gallery/profile.html')
