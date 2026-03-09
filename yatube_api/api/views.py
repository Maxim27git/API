from posts.models import Group,Post,Comment
from rest_framework import permissions
from api.permissions import AdminOnly
from rest_framework import viewsets
from api.serializers import GroupSerializers,PostSerializers,CommentSerializers
from django.shortcuts import get_object_or_404
class GroupViewSet(viewsets.ReadOnlyModelViewSet):
     queryset = Group.objects.all()
     serializer_class = GroupSerializers
     permission_classes = [AdminOnly]
class PostViewSet(viewsets.ModelViewSet):
     queryset = Post.objects.all()
     serializer_class = PostSerializers
     permission_classes = [permissions.IsAuthenticated]
     def perform_create(self, serializer):
          serializer.save(author=self.request.user)
class CommentViewSet(viewsets.ModelViewSet):
     #queryset = Comment.objects.all()
     serializer_class = CommentSerializers
     permission_classes = [permissions.IsAuthenticated]
     def perform_create(self, serializer):
          post=get_object_or_404(Post,pk=self.kwargs.get('post_id'))
          serializer.save(author=self.request.user,post=post)
     def get_queryset(self):
           post=get_object_or_404(Post,pk=self.kwargs.get('post_id'))
           return Comment.objects.filter(post=post)