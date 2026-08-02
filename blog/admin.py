from django.contrib import admin

from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at", "views_count")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "content")
