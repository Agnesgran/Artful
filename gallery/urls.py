from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.art_gallery, name='art_gallery'),
    path('upload/', views.upload_art, name='upload_art'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('upload/', views.upload_art, name='upload_art'),
    path('art/<int:pk>/', views.art_detail, name='art_detail'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_redirect, name='profile_redirect'),
    path('profile_detail/', views.profile, name='profile'),
    path('search/', views.search_results, name='search_results'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
