from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from category.models import SubCategory


# Create your models here.

# post
class Post(models.Model):
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, verbose_name='Select category for the Post', blank=False, null=False
    )
    title = models.TextField(blank=False, null=False, verbose_name='Head Line of the post')
    description = models.TextField(blank=True, null=True, verbose_name='Write a short description of your post')
    post = RichTextUploadingField(blank=True, null=True, verbose_name='Write your post here')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Date')
    priority = models.IntegerField(blank=False, null=False, verbose_name='Add priority of your post')
    read_time = models.IntegerField(blank=True, null=True, verbose_name='Approximate time to read this post')

    def __str__(self):
        return self.title


class Trending(models.Model):
    category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, verbose_name='Select Trending Category', blank=False, null=False
    )
    priority = models.IntegerField(blank=False, null=False, verbose_name='Add priority of your Category')

    def __str__(self):
        return self.category.name
