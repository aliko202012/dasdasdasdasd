from django.contrib import admin
from .models import Book
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','created_at','pages','logo']
    search_fields = ['id','title']
    list_filter = ['id','title']