from django.contrib import admin
from portfolio.models import Project

# Register your models here.
#admin.site.register(Project)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')
    ordering = ('title',)