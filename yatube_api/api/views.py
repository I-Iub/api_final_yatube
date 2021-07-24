# * При описании вьюсетов для некоторых моделей имеет смысл наследоваться от
# собственного базового вьюсета.
# * При попытке подписаться на самого себя, пользователь должен получить
# информативное сообщение об ошибке.
from rest_framework import viewsets

from posts.models import Comment, Follow, Group, Post
from .serializers import CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
