# Generated by Django 2.0.7 on 2020-06-01 11:46

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0015_tuihuoinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuihuoinfo',
            name='text',
            field=tinymce.models.HTMLField(default=None, max_length=200, verbose_name='退货理由'),
        ),
    ]