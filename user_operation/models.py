from django.db import models
from core.models import Pin
from users.models import UserInfo
from db.base_model import BaseModel

class UserOperation(BaseModel):
    """
    UserOperation
    """
    user = models.ForeignKey(UserInfo, verbose_name="用户")
    pin_num = models.IntegerField(verbose_name="Pin计数", default=0, help_text="pin数量")
    board_num = models.IntegerField(verbose_name="收藏夹计数", default=0, help_text="收藏夹计数")
    like_num = models.IntegerField(verbose_name="点赞计数", default=0, help_text="点赞计数")

    class Meta:
        verbose_name = "用户操作统计"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username

class UserLikes(BaseModel):
    """
    Pin
    """
    user = models.ForeignKey(UserInfo, verbose_name="用户")
    pin = models.ForeignKey(Pin, verbose_name="Pin", help_text="Pin图")

    class Meta:
        verbose_name = "用户点赞"
        verbose_name_plural = verbose_name
        unique_together = ("user", "pin",)

    def __str__(self):
        return self.user.username


