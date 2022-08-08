from category.models import Category, SubCategory
from post.models import Post, Trending
from quiz.models import Quiz
import json
import random


def navbar():
    categories = Category.objects.all().order_by('name')
    list_nav = []
    for category in categories:
        try:
            subcategories = SubCategory.objects.filter(parent=category).order_by('name')
            child = []
            if len(subcategories) != 0:
                for c in subcategories:
                    cx = Post.objects.filter(sub_category=c).count()
                    if cx > 0:
                        temp = {
                            'c_id': c.id,
                            'name': c.name
                        }
                        child.append(temp)
            else:
                child = []

        except:
            child = []
        temp1 = {
            'p_id': category.id,
            'menu': category.name,
            'submenu': child
        }
        list_nav.append(temp1)
    return list_nav


def listofpost(id):
    try:
        subcategory = SubCategory.objects.get(id=id)
        # print(subcategory.name)

        # posts = Post.objects.filter(sub_ == subdcategory.id).order_by('priority', 'pub_date')
        posts = Post.objects.filter(sub_category__name__exact=subcategory.name).order_by('priority', 'pub_date')
        list_post = []
        image_id = 1
        for post in posts:
            title_of_post = post.title
            count_of_questions = Quiz.objects.filter(title__iexact=title_of_post).count()
            # print(title_of_post)
            # print(count_of_questions)
            temp = {
                'id': post.id,
                'badgeTitle': post.sub_category.name,
                'postTitle': post.title,
                'postDescrition': post.description,
                'postDuration': post.read_time,
                'question': count_of_questions,
                'postImg': f"http://192.168.0.107:8080/media/post_card_image/cardimages{image_id}.jpg",
            }
            list_post.append(temp)
            if image_id >= 4:
                image_id = 1
            else:
                image_id += 1
    except:
        list_post = [{
            'error': 'no post found'
        }]
    json.dumps(list_post)
    return list_post


def trending_topics():
    trends = Trending.objects.all().order_by('priority')
    trending_topics_list = []
    for trend in trends:
        count = Post.objects.filter(sub_category__name__exact=trend.category.name).count()
        name = trend.category.name
        temp = {
            'trend_id': trend.category.id,
            'trend_name': name,
            'trend_count': count
        }
        trending_topics_list.append(temp)

    return trending_topics_list


def recent_post():
    posts = Post.objects.all().order_by('-pub_date')[0:9]
    posts_list = []
    for post in posts:
        temp = {
            'p_id': post.id,
            'p_title': post.title,
            'p_des': post.description
        }
        posts_list.append(temp)

    return posts_list


def stats():
    post_count = Post.objects.all().count()
    exercise_count = Quiz.objects.all().count()
    data = {
        'post_count': post_count,
        'exercise_count': exercise_count
    }
    return data

