from rest_framework import serializers
from blog.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'text', 'created_date', 'approved_comment')


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'comments')

    def update(self, instance, validated_data):
        print(instance)
        print(instance.id)
        print(instance.title)

        print(validated_data)
        return instance
