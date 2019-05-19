from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
from .adminforms import PostAdminForm
from lds_site.custom_site import custom_site
from lds_site.base_admin import BaseOwnerAdmin


class PostInline(admin.TabularInline):  # StackedInline  样式不同
    fields = ('title', 'desc')
    extra = 1  # 控制额外多几个
    model = Post


class CategoryOwnerFilter(admin.SimpleListFilter):
    """ 自定义过滤器只展示当前用户分类 """

    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        """返回要展示的内容和查询用的id"""
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        """
        根据 URL Query 的内容返回列表页数据，
        比如如果 URL 最后的 Query 是 ?parameter_name=1，那么这里的 self.value() 就是 1，根据1来过滤，
        返回已过滤的查询集。
        """
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status_show', 'owner',
        'created_time', 'operator',
    ]
    list_display_links = []

    list_filter = ['category', 'owner', CategoryOwnerFilter, ]
    search_fields = ['title', 'category__name', 'owner__username']
    show_full_result_count = True

    actions_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'created_time'
    # list_editable = ('title', )

    # 编辑页面
    save_on_top = True

    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('wide',),
            'fields': ('tags',),
        })
    )

    # 横向展示
    filter_horizontal = ('tags',)

    # 纵向展示
    # filter_vertical = ('tags',)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'

    class Media:
        css = {
            'all': ("https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css",),
        }
        js = ('https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js',)


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline, ]

    list_display = [
        'name',
        'status',
        'is_nav',
        'post_count',
    ]

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    pass
