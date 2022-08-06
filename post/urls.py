from django.urls import path, include, re_path
from . import views
app_name = 'post'

urlpatterns = [
    path('article_list/<str:id>', views.post_list, name='post_list'),
    path('article/<str:id>', views.post_details, name='post_details'),
]