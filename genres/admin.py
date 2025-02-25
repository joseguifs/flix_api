from django.contrib import admin
from genres.models import Genres

@admin.register(Genres)
class AdminGenres(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ['name']

# Register your models here.
