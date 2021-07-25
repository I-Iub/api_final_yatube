# * При описании вьюсетов для некоторых моделей имеет смысл наследоваться от
# собственного базового вьюсета.
# * При попытке подписаться на самого себя, пользователь должен получить
# информативное сообщение об ошибке.
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from posts.models import Follow, Group, Post
from .serializers import CommentSerializer, FollowSerializer, GroupSerializer
from .serializers import PostSerializer

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.author:
            raise PermissionDenied('Нельзя изменить чужой пост!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        if self.request.user != serializer.author:
            raise PermissionDenied('Нельзя удалить чужой пост!')
        super(PostViewSet, self).perform_destroy(serializer)


class CommentViewSet(viewsets.ModelViewSet):
    # queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.author:
            raise PermissionDenied('Нельзя изменить чужой комментарий!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        if self.request.user != serializer.author:
            raise PermissionDenied('Нельзя удалить чужой комментарий!')
        super(CommentViewSet, self).perform_destroy(serializer)


class FollowViewSet(viewsets.ModelViewSet):
    # queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Follow.objects.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
