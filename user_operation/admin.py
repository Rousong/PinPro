from django.contrib import admin

from .models import UserLikes, UserOperation


# Register your models here.
class UserLikesAdmin(admin.ModelAdmin):
    list_display = ('user', 'pin','update_time')
    list_filter = ["user", ]
    search_fields = ["pin", ]
    readonly_fields = ['user', 'pin', 'update_time']


class UserOperationAdmin(admin.ModelAdmin):
    list_display = ('user', 'pin_num', 'board_num', 'like_num',)
    readonly_fields = ['user']


admin.site.register(UserLikes, UserLikesAdmin)
admin.site.register(UserOperation, UserOperationAdmin)

