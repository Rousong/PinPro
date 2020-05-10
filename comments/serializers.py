from rest_framework import serializers

from .models import Comment
from core.models import Pin
from users.models import UserInfo

from core.serializers import PinSerializer
from users.serializers import UserSerializer


class CommentSerializer3(serializers.ModelSerializer):
    '''三级评论'''

    class Meta:
        model = Comment
        fields = ['id', 'parent_comment', 'content', 'published', 'author']


class CommentSerializer2(serializers.ModelSerializer):
    '''二级评论'''
    sub_comment = CommentSerializer3(many=True, required=False)

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    '''一级评论'''
    sub_comment = CommentSerializer2(many=True, required=False)

    # blog = serializers.ReadOnlyField(allow_blank=True)

    class Meta:
        model = Comment
        fields = '__all__'
