from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def gallery_home(request):
    return HttpResponse("Hello, Gallery!")

def home(request):
    return HttpResponse("Welcome to Artful!")

