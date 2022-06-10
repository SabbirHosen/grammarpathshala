from django.db import models
from .managers import CategoryManager, SubCategoryManager


class Node(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Nodes'


# proxy model category
class Category(Node):
    objects = CategoryManager()

    class Meta:
        proxy = True
        verbose_name_plural = 'Categories'


# proxy model subcategory
class SubCategory(Node):
    objects = SubCategoryManager()

    class Meta:
        proxy = True
        verbose_name_plural = 'Sub Categories'
