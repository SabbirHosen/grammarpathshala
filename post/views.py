from django.shortcuts import render
from .models import Post, SubCategory
from home.code import navbar, trending_topics
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from quiz.models import Quiz, QuizSet


# Create your views here.
def post_list(request, id):
    nav_list = navbar()
    trending_topics_list = trending_topics()
    # print(id)
    subcategory = SubCategory.objects.get(id=id)
    # posts = Post.objects.filter(sub_category_id=id).order_by('property', 'pub_date')
    posts = Post.objects.filter(sub_category__name__exact=subcategory.name).order_by('priority', 'pub_date')

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
    # print(list_post)
        # PAGINATOR start
        page = request.GET.get('page', 1)
        paginator = Paginator(list_post, 1)
        try:
            p_post = paginator.page(page)
        except PageNotAnInteger:
            p_post = paginator.page(1)
        except EmptyPage:
            p_post = paginator.page(paginator.num_pages)
    data = {
        'name': subcategory.name,
        'trending_topics': trending_topics_list,
        'nav': nav_list,
        'post_count': len(list_post),
        'posts': p_post
    }
    return render(request, template_name='blog.html', context=data)


def post_details(request, id):
    nav_list = navbar()
    trending_topics_list = trending_topics()
    post = Post.objects.get(id=id)
    posts_id = Post.objects.filter(sub_category__name__exact=post.sub_category.name).order_by('priority', 'pub_date').values('id')
    list_ids = [i['id'] for i in posts_id]
    # print('Post: ', list_ids)
    current_position = -1
    count = 0
    for i in list_ids:
        if str(i) == str(post.id):
            current_position = count
            break
        else:
            count += 1
    # print(current_position)
    try:
        has_next = list_ids[current_position + 1]
    except:
        has_next = None

    try:
        if current_position-1 == -1:
            has_previous = None
        else:
            has_previous = list_ids[current_position - 1]
    except:
        has_previous = None
    # print(f'N{has_next} P{has_previous}')
    try:
        quiz_exist = QuizSet.objects.filter(post_title__iexact=post.title, sub_category__name__iexact=post.sub_category.name)
        if quiz_exist.exists():
            exercise = post.title
        else:
            exercise = None
    except:
        exercise = None
    data = {
        'trending_topics': trending_topics_list,
        'nav': nav_list,
        'has_next': has_next,
        'has_previous': has_previous,
        'name': post.title,
        'post_duration': post.read_time,
        'post_des': post.description,
        'post': post.post,
        'badge': [post.sub_category.parent.name, post.sub_category.name],
        'exercise': exercise,

    }
    return render(request, template_name='blog-details.html', context=data)
