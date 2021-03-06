from django.db import models
from django.contrib import admin


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(default="")
    timestamp = models.DateField()


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)
