# Generated by Django 4.0.5 on 2022-06-09 15:42

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Head Line of the post')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Write a short description of your post')),
                ('post', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Write your post here')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('priority', models.IntegerField(verbose_name='Add priority of your post')),
                ('read_time', models.IntegerField(blank=True, null=True, verbose_name='Approximate time to read this post')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.subcategory', verbose_name='Select category for the Post')),
            ],
        ),
    ]