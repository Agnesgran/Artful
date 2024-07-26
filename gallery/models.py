from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Art(models.Model):
    ART_TYPE_CHOICES = (
        ('painting', 'Painting'),
        ('sculpture', 'Sculpture'),
        ('photograph', 'Photograph'),
        ('installation', 'Installation'),
        ('ceramic', 'Ceramic'),
        ('mixed_media', 'Mixed Media'),
    )

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='art_images/')
    art_type = models.CharField(max_length=20, choices=ART_TYPE_CHOICES)

    def __str__(self):
        return self.title


class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('user', 'User'),
        ('artist', 'Artist'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    preferred_medium = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')

    def __str__(self):
        return self.user.username