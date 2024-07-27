from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, ArtUploadForm
from .models import Profile, Art
from django.http import Http404

def home(request):
    return render(request, 'gallery/home.html')

def art_gallery(request):
    artworks = Art.objects.all()
    return render(request, 'gallery/art_gallery.html', {'artworks': artworks})

def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist.")
    return render(request, 'gallery/profile.html', {'profile': profile})

def update_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    
    return render(request, 'gallery/update_profile.html', {'form': form})


def upload_art(request):
    if request.method == 'POST':
        form = ArtUploadForm(request.POST, request.FILES)
        if form.is_valid():
            art = form.save(commit=False)
            art.artist = request.user
            art.save()
            return redirect('art_gallery')
    else:
        form = ArtUploadForm()
    
    return render(request, 'gallery/upload_art.html', {'form': form})
