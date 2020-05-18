from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Comment
from .serializers import CommentSerializer
from utils.pagination import Pagination


class CommentViewSet(viewsets.ModelViewSet):
    '''评论视图'''
    queryset = Comment.objects.all().order_by('-published')
    serializer_class = CommentSerializer
    # 指定自定义的分页class 这个会覆盖settings里面的分页设置
    pagination_class = Pagination
    filter_fields = '__all__'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'code': 20000,
            'items': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)