from django.urls import path
from .views import art_gallery

urlpatterns = [
    path('', art_gallery, name='art_gallery'),
]
