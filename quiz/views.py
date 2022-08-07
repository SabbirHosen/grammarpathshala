from django.shortcuts import render
from home.code import navbar, trending_topics
from .models import Quiz, QuizSet
from category.models import SubCategory


# Create your views here.
def quiz_list(request):
    nav_list = navbar()
    trending_topics_list = trending_topics()
    # quiz_sets = QuizSet.objects.all()
    sub_categories = SubCategory.objects.all().values('id', 'name')
    # print(sub_categories)
    all_data = []
    for category in sub_categories:
        # print(category['name'])
        try:
            quiz_sets = QuizSet.objects.filter(sub_category_id=category['id']).values('id', 'title_of_set')
            if quiz_sets.exists():
                # print(quiz_sets)
                list_of_set = []
                for sett in quiz_sets:
                    count = Quiz.objects.filter(title_id=sett['id']).count()
                    # print(count)
                    temp1 = {
                        'question_set_id': sett['id'],
                        'question_set_title': sett['title_of_set'],
                        'question_count': count
                    }
                    list_of_set.append(temp1)
                # count_question = Quiz.objects.filter(title_id=)
                temp = {
                    'category': category['name'],
                    'question_sets': list_of_set
                }
                all_data.append(temp)


        except:
            continue
    # count_set_of_quiz = len(quiz_sets)

    # for set in quiz_sets:
    #     temp = {
    #         'category': set.sub_category
    #     }
    data = {
        'nav': nav_list,
        'trending_topics': trending_topics_list,
        'sets': all_data,
        'count_set': QuizSet.objects.all().count()

    }
    # print(all_data)

    return render(request, template_name='exercise-home.html', context=data)


def do_exercise(request, id):
    pass



def do_exercise_from_post(request, id):
    pass
