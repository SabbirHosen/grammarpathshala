from django.urls import path, include, re_path
from . import views
app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('exercise/<slug:title>', views.do_exercise, name='do_exercise'),

]