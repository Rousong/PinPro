import django_filters
from django.db.models import Q

from .models import Pin
import datetime
from django.utils import timezone

# now_time = datetime.datetime.now() # 如果数据库保存的是UTC时间,程序不会蹦但是会提示你这不是本地时间
now_time = timezone.now()


class PinFilter(django_filters.rest_framework.FilterSet):
    """
    Pin的过滤类
    """
    # Filter.name renamed to Filter.field_name (#792) from django-filter==2.0 onwards, use field_name instead of name
    submitter__username = django_filters.CharFilter(field_name="submitter__username", help_text="用户名")
    tags__name = django_filters.CharFilter(field_name="tags__name", help_text="标签名")

    # field_name: 需要筛选的模型字段的名称，使用django的 “__”语法遍历“关系路径”来过滤相关模型上的字段.
    # https://qiita.com/okoppe8/items/77f7f91f6878e3f324cc

    top_liked = django_filters.CharFilter(method='top_liked_filter', help_text="点赞排名")

    def top_liked_filter(self, queryset, name, value):
        if value == "week":
            # 当前天 显示当前日期是本周第几天
            day_num = now_time.isoweekday()
            # 计算当前日期所在周一
            monday = (now_time - datetime.timedelta(days=day_num))
            # 查询一周内的数据
            week_pins = queryset.filter(Q(published__range=(monday, now_time)) & ~Q(likes_num=0)).order_by("likes_num")
            return week_pins
        elif value == "month":
            month_pins = queryset.filter(Q(published__month=now_time.month) & ~Q(likes_num=0)).order_by("likes_num")
            return month_pins
        elif value == "year":
            year_pins = queryset.filter(Q(published__year=now_time.year) & ~Q(likes_num=0)).order_by("likes_num")
            return year_pins

    class Meta:
        model = Pin
        fields = ['submitter']
