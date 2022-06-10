from django.contrib import admin
from .models import Quiz


# Register your models here.

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_category', 'question')
    list_editable = ['sub_category']
    list_filter = ('sub_category',)
    search_fields = ['title', 'question']


admin.site.register(Quiz, QuizAdmin)