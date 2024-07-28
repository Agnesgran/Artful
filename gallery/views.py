from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, ArtUploadForm, CommentForm
from .models import Profile, Art, Comment
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

@login_required
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

    def art_detail(request, pk):
    art = get_object_or_404(Art, pk=pk)
    comments = art.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.art = art
            comment.user = request.user
            comment.save()
            return redirect('art_detail', pk=art.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'gallery/art_detail.html', {'art': art, 'comments': comments, 'comment_form': comment_form})
