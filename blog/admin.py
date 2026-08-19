from django.contrib import admin
from .models import Blog
from django.core.cache import cache

#function for clearing the cache from the admin panel
def clear_cache(modeladmin, request, queryset):
    cache.clear()
    modeladmin.message_user(request, "Cache cleared successfully.")

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'category')
    list_filter = ('category', 'created_at', 'updated_at')
    actions=['clear_cache']