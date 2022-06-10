from django.db import models
from category.models import SubCategory


# Create your models here.

class Quiz(models.Model):
    choice = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    ]
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, verbose_name='Select category for the Question', blank=False, null=False
    )
    title = models.TextField(blank=False, null=False, verbose_name='Write the Title fo Your Quiz')
    question = models.TextField(blank=False, null=False, verbose_name='Question')
    option_a = models.CharField(blank=False, null=False, verbose_name='Option A', max_length=424)
    option_b = models.CharField(blank=False, null=False, verbose_name='Option B', max_length=424)
    option_c = models.CharField(blank=False, null=False, verbose_name='Option C', max_length=424)
    option_d = models.CharField(blank=True, null=True, verbose_name='Option D', max_length=424)
    answer = models.CharField(blank=False, null=False, verbose_name='Select write answer of the question',
                              max_length=2, choices=choice
                              )

    def __str__(self):
        return self.title
