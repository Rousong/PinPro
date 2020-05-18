from django.contrib import admin

from .models import UserLikes, UserOperation


# Register your models here.
class UserLikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pin', 'update_time',)
    list_filter = ["user", "pin", ]

class UserOperationAdmin(admin.ModelAdmin):
    list_display = ('user', 'pin_num', 'board_num', 'like_num',)


admin.site.register(UserLikes, UserLikesAdmin)
admin.site.register(UserOperation, UserOperationAdmin)