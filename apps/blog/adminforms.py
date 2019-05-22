from dal import autocomplete
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from django import forms

from .models import Category, Tag, Post


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    # 这个在 xadmin 上面无效，让我们试试 admin 是否可以
    # category = forms.ModelChoiceField(
    #     queryset=Category.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='category-autocomplete'),
    #     label='分类',
    # )
    # tags = forms.ModelMultipleChoiceField(
    #     queryset=Tag.objects.all(),
    #     widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
    #     label='标签',
    # )
    content = forms.CharField(widget=CKEditorUploadingWidget(), label='正文', required=True)

    class Meta:
        model = Post
        fields = ('category', 'tags', 'desc', 'title', 'content', 'status')
