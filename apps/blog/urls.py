from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.blog.views import (
    BlogCreateView,
    BlogDetailView,
    BlogItemView,
    BlogListView,
    CategoryViewSet,
    CommentCreateView,
)

router = DefaultRouter(trailing_slash=False)
router.register(
    r"blog/categories",
    CategoryViewSet,
    basename="category",
)

urlpatterns = [
    path("blog", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>", BlogItemView.as_view(), name="blog_item"),
    path("blog/create/", BlogCreateView.as_view(), name="blog-create"),
    path("comment/create/", CommentCreateView.as_view(), name="comment-create"),
    path("blog/blog/<int:id>/", BlogDetailView.as_view(), name="blog-detail"),
    *router.urls,
]
