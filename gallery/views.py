from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages framework
from .forms import ProfileUpdateForm, ArtUploadForm, CommentForm
from .models import Profile, Art, Comment
from django.http import Http404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

def home(request):
    return render(request, 'gallery/home.html')

def art_gallery(request):
    artworks = Art.objects.all()
    return render(request, 'gallery/art_gallery.html', {'artworks': artworks})

@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist.")
    return render(request, 'gallery/profile.html', {'profile': profile})

def profile_redirect(request):
    if request.user.is_authenticated:
        return redirect('profile')

def update_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
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
            messages.success(request, 'Art uploaded successfully!')
            return redirect('art_gallery')
    else:
        form = ArtUploadForm()
    
    return render(request, 'gallery/upload_art.html', {'form': form})

def art_detail(request, pk):
    art = get_object_or_404(Art, pk=pk)
    comments = art.comments.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.art = art
            comment.user = request.user
            comment.save()
            messages.success(request, 'Your comment has been posted!')
            return redirect('art_detail', pk=art.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'gallery/art_detail.html', {'art': art, 'comments': comments, 'comment_form': comment_form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('home')

def search_results(request):
    query = request.GET.get('q', '')
    if query:
        artworks = Art.objects.filter(title__icontains=query) | Art.objects.filter(artist__username__icontains=query)
    else:
        artworks = Art.objects.none()
    return render(request, 'gallery/search_results.html', {'artworks': artworks, 'query': query})
