from django.contrib import admin
from .models import Post, Comment

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Comment)
