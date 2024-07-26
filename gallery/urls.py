from django.urls import path
from .views import art_gallery, profile

urlpatterns = [
    path('', art_gallery, name='art_gallery'),
    path('profile/', profile, name='profile'),
]
