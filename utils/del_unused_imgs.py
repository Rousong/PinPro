#!/usr/bin/env python
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'pinry.settings.development'  # 配置系统变量
import django

django.setup()

from django.db.models import Q

from django_images.models import Image
from core.models import Pin

# 获取pin表的image字段（id）集合 获取image表的id集合
set_a = set(Pin.objects.all().values_list('image', flat=True))
set_b = set(Image.objects.all().values_list('id', flat=True))

# 获取并集
del_items = set_a & set_b

# 筛选出图片TBL的并集以外的item，也就是没有用到的图片
pics = Image.objects.filter(~Q(id__in=del_items))

print("未发布的图片有:{}张".format(pics.count()))
# 打印id和地址，并且修改is_published字段，更新表
for pic in pics:
    if pic.is_published is True:
        print("ID:{}  URL:{}".format(pic.id, pic.image))
        pic.is_published = False
        pic.save()
    else:
        print("ID:{}  URL:{} 已在未发布标签".format(pic.id, pic.image))
