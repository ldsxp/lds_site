from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'ldsSite'
    site_title = 'ldsSite管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
