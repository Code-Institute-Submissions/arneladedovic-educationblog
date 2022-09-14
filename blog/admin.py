from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Fields with summernote editor in adminpage
    """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on',)
    search_fields = ['title', 'content']
    list_display = ('title', 'slug', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Fields for display in adminpage
    """
    list_filter = ('created_on',)
    search_fields = ['name', 'body']
    list_display = ('name', 'body', 'created_on', 'post')