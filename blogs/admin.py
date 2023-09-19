from django.contrib import admin
from .models import Blog
from .models import Comment
# Register your models here.
@admin.register(Blog)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'picture', 'category', 'datetime', 'heading', 'content']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'message', 'created_on']
