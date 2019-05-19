from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'category', 'status_show', 'owner',
        'created_time', 'operator',
    ]
    list_display_links = []

    list_filter = ['category', 'owner']
    search_fields = ['title', 'category__name', 'owner__username']
    show_full_result_count = True

    actions_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'created_time'
    # list_editable = ('title', )

    # 编辑页面
    save_on_top = True

    fieldsets = (  # 跟fields互斥
        ('基础配置', {
            'fields': (('category', 'title'), 'content')
        }),
        ('高级配置', {
            'fields': ('tags',),
        }),
    )

    filter_horizontal = ('tags',)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

    list_display = [
        'name',
        'status',
        'is_nav',
        'post_count',
    ]

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
