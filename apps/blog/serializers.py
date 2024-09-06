from rest_framework import serializers

from apps.blog.models import Blog, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    blog_id = serializers.PrimaryKeyRelatedField(source="blog", queryset=Blog.objects.all())

    class Meta:
        model = Comment
        fields = ["text", "blog_id"]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
