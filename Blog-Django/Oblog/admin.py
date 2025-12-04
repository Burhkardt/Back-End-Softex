from django.contrib import admin
from .models import Post

# Register your models here.
class PostColumns(admin.ModelAdmin):
    list_display = ('Titulo', 'Autor')
admin.site.register(Post, PostColumns)