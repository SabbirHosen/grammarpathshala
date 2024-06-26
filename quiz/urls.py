from django.urls import path, include, re_path
from . import views
app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('exercise/<int:id>', views.do_exercise, name='do_exercise'),
    path('result/<int:id>', views.check_answer, name='check_answer')

]