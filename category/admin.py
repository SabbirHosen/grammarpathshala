from django.contrib import admin
from .models import Category, SubCategory
from post.models import Post

# Register your models here.


class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = (
        (
            None, {
                'fields': ('name',)
            }
        ),
    )
    inlines = (SubCategoryInline,)


admin.site.register(Category, CategoryAdmin)


class PostInline(admin.TabularInline):
    model = Post
    extra = 1


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('parent', 'name', 'post_count')
    # list_editable = ('parent',)
    fieldsets = (
        (
            None, {
                'fields': ('name',)
            }
        ),
    )
    # inlines = (PostInline,)

    def post_count(self, obj):
        return obj.post_set.count()

    def get_ordering(self, request):
        return 'parent', 'name'


