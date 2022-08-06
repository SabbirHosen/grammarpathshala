from django.contrib import admin
from .models import Post, Trending


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_category', 'priority')
    list_editable = ['sub_category', 'priority']
    list_filter = ('sub_category', 'pub_date')
    ordering = ['priority']
    search_fields = ['title', 'sub_category', 'description']


class TrendingAdmin(admin.ModelAdmin):
    list_display = ('category', 'priority')
    list_editable = ['priority']
    ordering = ['priority']


admin.site.register(Post, PostAdmin)
admin.site.register(Trending, TrendingAdmin)
