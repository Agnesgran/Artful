from django.shortcuts import render
from .models import Art
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm

def home(request):
    return render(request, 'gallery/home.html')

def art_gallery(request):
    artworks = Art.objects.all()
    return render(request, 'gallery/art_gallery.html', {'artworks': artworks})

def profile(request):
    return render(request, 'gallery/profile.html')

def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    
    return render(request, 'gallery/update_profile.html', {'form': form})