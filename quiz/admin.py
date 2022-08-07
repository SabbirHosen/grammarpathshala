from django.contrib import admin
from .models import Quiz, QuizSet


# Register your models here.

class QuizAdmin(admin.ModelAdmin):
    model = Quiz
    list_display = ('title', 'question', 'post_title', 'sub_category')
    search_fields = ['title__title_of_set', 'question']

    def post_title(self, obj):
        return obj.title.post_title

    def sub_category(self, obj):
        return obj.title.sub_category

    post_title.admin_order_field = 'title'  # Allows column order sorting
    post_title.short_description = 'Post Title'  # Renames column head
    sub_category.admin_order_field = 'title'  # Allows column order sorting
    sub_category.short_description = 'Sub Category'  # Renames column head


class QuizSetAdmin(admin.ModelAdmin):
    list_display = ('title_of_set', 'sub_category', 'post_title')
    list_editable = ['sub_category', 'post_title']
    list_filter = ('sub_category',)
    search_fields = ['title_of_set']


admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizSet, QuizSetAdmin)
