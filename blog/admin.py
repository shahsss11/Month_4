from django.contrib import admin
from . import models

@admin.register(models.Blog)
class BlogAmin(admin.ModelAdmin):
    exclude = ('views',)