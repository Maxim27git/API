from rest_framework import serializers
from posts.models import Group,Post,Comment

class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields=('id','title','slug','description')
class PostSerializers(serializers.ModelSerializer):
    author=serializers.SlugRelatedField(
         slug_field='username',
         read_only=True
     )
    class Meta:
        model=Post
        fields=('id', 'text','author','image','group','pub_date')
class CommentSerializers(serializers.ModelSerializer):
    author=serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    class Meta:
        model=Comment
        fields=('id','text','author','post','created')
        read_only_fields=('post',)
