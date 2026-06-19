from django.contrib import admin
from .models import Category, Article
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')
    search_fields = ('name', 'description')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_to_read', 'category', 'counter', 'author', 'created_at')
    list_filter = ('category', 'author')
    search_fields = ('title', 'content', 'author')

