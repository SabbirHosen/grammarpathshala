from django.contrib import admin
from .models import Quiz, QuizSet


# Register your models here.

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'question')
    search_fields = ['title', 'question']


class QuizSetAdmin(admin.ModelAdmin):
    list_display = ('title_of_set', 'sub_category', 'post_title')
    list_editable = ['sub_category', 'post_title']
    list_filter = ('sub_category',)
    search_fields = ['title_of_set']


admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizSet, QuizSetAdmin)
