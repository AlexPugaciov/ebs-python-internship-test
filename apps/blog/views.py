from rest_framework import generics, viewsets
from rest_framework.generics import CreateAPIView, GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from apps.blog.models import Blog, Category, Comment
from apps.blog.serializers import BlogSerializer, CategorySerializer, GetCommentSerializer, POSTCommentSerializer
from apps.common.permissions import ReadOnly


class BlogCreateView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = POSTCommentSerializer


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        blog = self.get_object()
        comments = blog.comments.all()
        blog_data = BlogSerializer(blog).data
        blog_data.update(
            {
                "comments": GetCommentSerializer(comments, many=True).data,
            }
        )
        return Response(
            {
                "blog": blog_data,
            }
        )


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly,)

    def get(self, request: Request) -> Response:
        blogs = Blog.objects.all()
        return Response(self.get_serializer(blogs, many=True).data)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly, IsAuthenticated)

    def get(self, request: Request, pk: int) -> Response:
        blog: Blog = get_object_or_404(Blog.objects.all(), pk=pk)
        return Response(self.get_serializer(blog).data)
