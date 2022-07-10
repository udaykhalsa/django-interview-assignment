from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display = ['name', 'author']
    search_fields = ['name', 'author']

admin.site.register(Books, BooksAdmin)