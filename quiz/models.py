from django.db import models
from category.models import SubCategory
from post.models import Post


# Create your models here.
class QuizSet(models.Model):
    title_of_set = models.TextField(blank=False, null=False, verbose_name='Write the Title of Your Quiz')
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, verbose_name='Select category for the Quiz Set', blank=False, null=False
    )
    post_title = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Select Post Title', blank=True, null=True
    )

    def __str__(self):
        return self.title_of_set


class Quiz(models.Model):
    choice = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    ]

    title = models.ForeignKey(
        QuizSet, on_delete=models.CASCADE, verbose_name='Select the Title of Your Quiz', blank=False, null=False
    )
    question = models.TextField(blank=False, null=False, verbose_name='Question')
    option_a = models.CharField(blank=False, null=False, verbose_name='Option A', max_length=424)
    option_b = models.CharField(blank=False, null=False, verbose_name='Option B', max_length=424)
    option_c = models.CharField(blank=False, null=False, verbose_name='Option C', max_length=424)
    option_d = models.CharField(blank=True, null=True, verbose_name='Option D', max_length=424)
    answer = models.CharField(blank=False, null=False, verbose_name='Select write answer of the question',
                              max_length=2, choices=choice
                              )

    def __str__(self):
        return self.title.title_of_set
