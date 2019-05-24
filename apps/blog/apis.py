from rest_framework import viewsets
# from rest_framework.permissions import IsAdminUser

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """ 提供文章接口 """
    serializer_class = PostSerializer
    queryset = Post.latest_posts()
    # permission_classes = [IsAdminUser]  # 权限验证
