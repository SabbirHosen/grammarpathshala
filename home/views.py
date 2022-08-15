from django.shortcuts import render, redirect
from .code import navbar, trending_topics, recent_post, stats
from category.models import Category, SubCategory
from post.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    nav_list = navbar()
    trending_topics_list = trending_topics()
    recent_posts = recent_post()
    statistic = stats()
    data = {
        'nav': nav_list,
        'trending_topics': trending_topics_list,
        'recent_posts': recent_posts,
        'statistic': statistic
    }
    # print(recent_posts)
    return render(request, template_name='base/index_test.html', context=data)


def error_handler(request, exception=None):
    return redirect('home:home')

def search(request):
    if request.method == 'GET':
        nav_list = navbar()
        trending_topics_list = trending_topics()
        text = request.GET['search_text']
        posts = Post.objects.filter(sub_category__name__icontains=text) | Post.objects.filter(title__icontains=text)
        posts = posts.order_by('priority', 'pub_date')[0:10]
        list_post = []
        for post in posts:
            title_of_post = post.title
            temp = {
                'id': post.id,
                'badgeTitle': [post.sub_category.parent.name, post.sub_category.name],
                'postTitle': post.title,
                'postDescription': post.description,
                'postDuration': post.read_time,
            }
            list_post.append(temp)
        data = {
            'name': 'Search for ' + text,
            'form_value': text,
            'trending_topics': trending_topics_list,
            'nav': nav_list,
            'post_count': len(list_post),
            'posts': list_post,
            'search_for': text
        }
        return render(request, template_name='search_blog.html', context=data)
    return redirect('/')

