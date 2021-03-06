# Generated by Django 2.2.1 on 2019-05-19 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebar',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '展示'), (0, '隐藏')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='link',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='link',
            name='weight',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, help_text='权重高展示顺序靠前', verbose_name='权重'),
        ),
    ]
