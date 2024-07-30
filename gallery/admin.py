from django.contrib import admin
from .models import Art

# Register your models here.

from django.contrib import admin
from .models import Art

@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'price', 'available', 'art_type']
    list_filter = ['art_type', 'available']
    search_fields = ['title', 'description', 'artist__username']

    fieldsets = (
        (None, {
            'fields': ('title', 'artist', 'description', 'price', 'available', 'image', 'art_type')
        }),
    )
