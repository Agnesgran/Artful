from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('user', 'User'),
        ('artist', 'Artist'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    preferred_medium = models.CharField(max_length=100, blank=True)
    user_type = models.CharField(
             max_length=10, choices=USER_TYPE_CHOICES,
             default='user')

    def __str__(self):
        return self.user.username


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Art(models.Model):
    is_featured = models.BooleanField(default=False)
    ART_TYPE_CHOICES = (
        ('painting', 'Painting'),
        ('sculpture', 'Sculpture'),
        ('photograph', 'Photograph'),
        ('installation', 'Installation'),
        ('ceramic', 'Ceramic'),
        ('mixed_media', 'Mixed Media'),
    )

    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='art_images/')
    art_type = models.CharField(max_length=20, choices=ART_TYPE_CHOICES)

    def __str__(self):
        return self.title


def get_profile(user):
    profile, created = Profile.objects.get_or_create(user=user)
    return profile


User.profile = property(get_profile)


class Comment(models.Model):
    art = models.ForeignKey(
        Art, on_delete=models.CASCADE,
        related_name='comments'
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.art.title}'