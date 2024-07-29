# gallery/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, login_success

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.art_gallery, name='art_gallery'),
    path('upload/', views.upload_art, name='upload_art'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('art/<int:pk>/', views.art_detail, name='art_detail'),
    path('login/', CustomLoginView.as_view(), name='login'), 
    path('login/success/', login_success, name='login_success'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('signup_success/', views.signup_success, name='signup_success'),
    path('gallery/load-more/', views.load_more_artworks, name='load_more_artworks'),
    path('logout_success/', views.logout_success, name='logout_success'),
    path('search/', views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
