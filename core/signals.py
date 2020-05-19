from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_images.models import Image
from .models import Pin, Board
from user_operation.models import UserOperation


# 如果想要让signal信号生效  需要在app.py里面注册一下
@receiver(post_save, sender=Board)
def create_user_board(sender, instance=None, created=False, **kwargs):
    if created:
        # 操作统计用
        user_operation = UserOperation.objects.get(user=instance.submitter)
        user_operation.board_num += 1
        user_operation.save()


@receiver(post_delete, sender=Board)
def delete_user_board(sender, instance=None, created=False, **kwargs):
    # 操作统计用
    user_operation = UserOperation.objects.get(user=instance.submitter)
    user_operation.board_num -= 1
    user_operation.save()


@receiver(post_save, sender=Pin)
def create_user_pin(sender, instance=None, created=False, **kwargs):
    if created:
        # 操作统计用
        user_operation = UserOperation.objects.get(user=instance.submitter)
        user_operation.pin_num += 1
        user_operation.save()


@receiver(post_delete, sender=Pin)
def delete_pin_images(sender, instance, **kwargs):

    user_operation = UserOperation.objects.get(user=instance.submitter)
    user_operation.pin_num -= 1
    user_operation.save()

    try:
        instance.image.delete()
    except Image.DoesNotExist:
        pass
