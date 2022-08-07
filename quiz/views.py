from django.shortcuts import render, redirect
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
    nav_list = navbar()
    trending_topics_list = trending_topics()
    questions = Quiz.objects.filter(title_id=id)
    # title = QuizSet.objects.filter()
    question_list = []
    count = 1
    for question in questions:
        temp = {
            'set_title': question.title,
            'count': count,
            'question_id': question.id,
            'question': question.question,
            'option_A': question.option_a,
            'option_B': question.option_b,
            'option_C': question.option_c,
            'option_D': question.option_d,
        }
        question_list.append(temp)
        count += 1
    data = {
        'nav': nav_list,
        'trending_topics': trending_topics_list,
        're_id': id,
        'num_of_questions': len(questions),
        'name': question_list[0]['set_title'],
        'questions': question_list

    }
    print(question_list[0]['set_title'])
    return render(request, template_name='exercise.html', context=data)


def do_exercise_from_post(request, id):
    pass


def check_answer(request, id):
    if request.method == 'POST':
        nav_list = navbar()
        trending_topics_list = trending_topics()
        questions = Quiz.objects.filter(title_id=id)
        question_list = []
        count = 1
        correct = 0
        for question in questions:
            gen_id = 'q_'+str(question.id)
            answer = request.POST[gen_id]
            visible = {'A': '', 'B': '', 'C': '', 'D': ''}
            ch = {'A': '', 'B': '', 'C': '', 'D': ''}
            print(answer)
            if str(answer).strip().lower() == str(question.answer).strip().lower():
                correct += 1
                visible[str(question.answer).strip()] = 'right-ans'
                ch[str(question.answer).strip()] = 'checked'
            else:
                visible[str(answer).strip()] = 'wrong-ans'
                visible[str(question.answer).strip()] = 'right-ans'
                ch[str(answer).strip()] = 'checked'
                ch[str(question.answer).strip()] = 'checked'

            temp = {
                'set_title': question.title,
                'count': count,
                'question_id': question.id,
                'question': question.question,
                'option_A': question.option_a,
                'option_B': question.option_b,
                'option_C': question.option_c,
                'option_D': question.option_d,
                'answer': question.answer,
                'visible': visible,
                'checked': ch
            }
            question_list.append(temp)
            count += 1
            print(temp)

        message = {
            'percent': (correct/len(questions))*100,
            'tag': 'Congratulations!',
            'msg': 'You did a great job in the test',
        }
        data = {
            'nav': nav_list,
            'trending_topics': trending_topics_list,
            'num_of_questions': len(questions),
            'name': question_list[0]['set_title'],
            'questions': question_list,
            'result': message
        }
        return render(request, template_name='answer.html', context=data)
    return redirect('/')
