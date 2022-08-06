from django.shortcuts import render
from .code import navbar, trending_topics, recent_post
from category.models import Category, SubCategory


# Create your views here.
def home(request):
    nav_list = navbar()
    trending_topics_list = trending_topics()
    recent_posts = recent_post()
    data = {
        'nav': nav_list,
        'trending_topics': trending_topics_list,
        'recent_posts': recent_posts
    }
    # print(recent_posts)
    return render(request, template_name='base/indextest.html', context=data)
