from django.contrib import admin

from apps.blog.models import Blog, Category, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "enabled")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("blog", "text")


admin.site.register(Comment, CommentAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
