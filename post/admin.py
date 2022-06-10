from django.contrib import admin
from .models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_category', 'priority')
    list_editable = ['sub_category', 'priority']
    list_filter = ('sub_category', 'pub_date')
    ordering = ['priority']
    search_fields = ['title', 'sub_category', 'description']


admin.site.register(Post, PostAdmin)
