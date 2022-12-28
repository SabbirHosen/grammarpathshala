from django.urls import path, include, re_path
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
]
