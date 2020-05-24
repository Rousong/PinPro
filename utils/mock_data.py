#!/usr/bin/env python
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'pinry.settings.development'  # 配置系统变量
import django

django.setup()

import random
from core.models import Pin
from users.models import UserInfo
from django_images.models import Image

user1 = UserInfo.objects.get(id=1)
user2 = UserInfo.objects.get(id=2)
user3 = UserInfo.objects.get(id=3)

image1 = Image.objects.get(id=random.randint(1, 10))
image2 = Image.objects.get(id=random.randint(1, 10))
image3 = Image.objects.get(id=random.randint(1, 10))
image4 = Image.objects.get(id=6)
image5 = Image.objects.get(id=7)
image6 = Image.objects.get(id=8)

for i in range(1, 5000):

    pin1 = Pin()
    pin1.submitter = user1
    pin1.image = image1
    pin1.tags = ["xx", "xxx"]

    pin2 = Pin()
    pin2.submitter = user2
    pin2.image = image2
    pin2.tags = ["xx", "xxx"]
    pin2.likes_num = random.randint(0, 50)

    pin3 = Pin()
    pin3.submitter = user3
    pin3.image = image3
    pin3.tags = ["xx", "xxx"]
    pin3.likes_num = random.randint(0, 500)

    pin4 = Pin()
    pin4.submitter = user1
    pin4.image = image4
    pin4.tags = ["xx", "xxx"]

    pin5 = Pin()
    pin5.submitter = user2
    pin5.image = image5
    pin5.tags = ["xx", "xxx"]
    pin5.likes_num = random.randint(0, 50)

    pin6 = Pin()
    pin6.submitter = user3
    pin6.image = image6
    pin6.tags = ["xx", "xxx"]
    pin6.likes_num = random.randint(0, 500)

    querysetlist = []
    querysetlist.append(pin1)
    querysetlist.append(pin2)
    querysetlist.append(pin3)
    querysetlist.append(pin4)
    querysetlist.append(pin5)
    querysetlist.append(pin6)
    Pin.objects.bulk_create(querysetlist)
    print(i)