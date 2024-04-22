from django.shortcuts import get_object_or_404
from rest_framework import generics, filters, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination

from .serializers import (PostSerializer, GroupSerializer,
                          CommentSerializer, FollowSerializer)
from .permissions import IsOwnerOrReadOnly
from posts.models import Post, Group, Comment, Follow


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    @property
    def get_post(self):
        return get_object_or_404(
            Post,
            pk=self.kwargs['post_id']
        )

    def get_queryset(self):
        return self.get_post.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post
        )


class FollowViewSet(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()
