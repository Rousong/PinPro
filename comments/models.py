from django.db import models
from db.base_model import BaseModel
from django.conf import settings

from core.models import Pin
from users.models import UserInfo


class Comment(BaseModel):
    '''评论'''
    content = models.TextField(max_length=255, verbose_name='评论内容')
    pin = models.ForeignKey(Pin, related_name='comments', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(UserInfo, related_name="comments", to_field="id", on_delete=models.CASCADE)
    parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="父类目级别", help_text="父目录", related_name='sub_comment', default='')

    class Meta:
        db_table = 'posts_comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:50]