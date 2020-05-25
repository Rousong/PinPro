from django.contrib import admin

from .models import  Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 2


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'pin', 'author', 'content', 'parent_comment',  'published', ]
    readonly_fields = ['pin', 'author','parent_comment']
    # list_filter = ['pin', 'author', 'parent_comment',]

