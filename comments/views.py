from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    '''评论视图'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
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