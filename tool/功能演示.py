# Django 环境设置 ==================================================================
from ilds.django.util import django_setup

django_setup(r'lds_site', site_path=None)
# ------------------------------------------------------------------ Django 环境设置

from blog.models import Post

for obj in Post.objects.all():
    print(obj.to_dict())
