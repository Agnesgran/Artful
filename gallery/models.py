from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Art(models.Model):
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