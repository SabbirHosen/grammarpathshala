from django.shortcuts import render
from home.code import navbar, trending_topics
from .models import Quiz


# Create your views here.
def quiz_list(request):
    nav_list = navbar()
    trending_topics_list = trending_topics()
    data = {
        'nav': nav_list,
        'trending_topics': trending_topics_list,
    }
    return render(request, template_name='exercise-home.html', context=data)


def do_exercise(request, title):
    pass
