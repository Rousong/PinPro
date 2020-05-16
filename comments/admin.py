from django.contrib import admin

from .models import  Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 2


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['pin', 'author', 'content', 'parent_comment',  'published', ]
    list_filter = ['pin', 'author', 'parent_comment',]

