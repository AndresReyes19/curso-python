from django.contrib import admin
from movies.models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Movie, MovieAdmin)