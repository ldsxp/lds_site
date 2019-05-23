# Generated by Django 2.2.1 on 2019-05-23 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190521_2219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-id'], 'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
        migrations.AddField(
            model_name='post',
            name='is_md',
            field=models.BooleanField(default=False, verbose_name='markdown语法'),
        ),
    ]
