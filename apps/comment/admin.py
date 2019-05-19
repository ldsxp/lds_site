from django.contrib import admin

from .models import Comment
from lds_site.custom_site import custom_site


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'nickname', 'content', 'website', 'created_time')
