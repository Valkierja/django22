import imp
from django.urls import path
from . import views
from django.shortcuts import redirect
from django.urls import path, include

app_name = 'article'
urlpatterns = [
    path('', lambda request: redirect('article-list/', permanent=True)),

    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_details, name='article_detail'),
]
