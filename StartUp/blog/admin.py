from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    fields = ('title', 'slug')
    prepopulated_fields = {"slug": ('title', )}

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')
    fields = ("title", "slug", "image", "description", "author", "category", "tag")
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ('created', "updated", "category", "author")
# admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)