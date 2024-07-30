from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileUpdateForm, ArtUploadForm, CommentForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, Art, Comment
from django.http import JsonResponse
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.messages import get_messages
from .forms import ProfileForm


def home(request):
    return render(request, 'gallery/home.html')


def art_gallery(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        artworks = Art.objects.all()

        data = {
            'artworks': list(artworks.values(
                'id', 'title', 'image', 'description',
                'price', 'artist__username'))
        }
        return JsonResponse(data)

    artworks = Art.objects.all()
    return render(request, 'gallery/art_gallery.html', {'artworks': artworks})


@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        raise Http404("Profile does not exist.")

    return render(request, 'gallery/profile.html', {'profile': profile})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)

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


@login_required
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

            # Handle AJAX requests
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                data = {
                    'success': True,
                    'comment': {
                        'user': comment.user.username,
                        'text': comment.text,
                        'created_at': comment.created_at.strftime(
                            '%Y-%m-%d %H:%M:%S')
                    }
                }
                return JsonResponse(data)

            return redirect('art_detail', pk=art.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'gallery/art_detail.html', {
        'art': art, 'comments': comments, 'comment_form': comment_form})


def delete_art(request, pk):
    art = get_object_or_404(Art, pk=pk)
    if request.method == 'POST':
        art.delete()
        return redirect('art_gallery')
    return render(request, 'gallery/delete_art.html', {'art': art})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('signup_success')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def signup_success(request):
    return render(request, 'accounts/signup_success.html')


def logout_view(request):
    auth_logout(request)
    return redirect('logout_success')


def logout_success(request):
    return render(request, 'accounts/logout_success.html')


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        remember_me = self.request.POST.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(CustomLoginView, self).form_valid(form)


def login_success(request):
    storage = get_messages(request)
    messages = [str(message) for message in storage]
    return render(request, 'accounts/login_success.html', {
        'messages': messages})


def search_results(request):
    query = request.GET.get('query')
    if query:
        results = Art.objects.filter(title__icontains=query)
    else:
        results = Art.objects.none()
    return render(request, 'gallery/search_results.html', {'results': results})


def load_more_artworks(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        artworks = Art.objects.all()
        data = {
            'artworks': list(artworks.values(
                      'id', 'title', 'image', 'description', 'price',
                      'artist__username'))
        }
        return JsonResponse(data)
    return JsonResponse({'error': 'Invalid request'}, status=400)