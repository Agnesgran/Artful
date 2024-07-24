from django.shortcuts import render
from django.http import HttpResponse
from .models import Art

def gallery_home(request):
    return HttpResponse("Hello, Gallery!")

def home(request):
    return HttpResponse("Welcome to Artful!")

def art_gallery(request):
    artworks = Art.objects.all()
    return render(request, 'gallery/art_gallery.html', {'artworks': artworks})
