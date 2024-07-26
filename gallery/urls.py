from django.urls import path
from .views import art_gallery, profile
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', art_gallery, name='art_gallery'),
    path('profile/', profile, name='profile'),
    path('profile/', views.profile_view, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
]
