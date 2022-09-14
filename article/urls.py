import imp
from django.urls import path
from . import views
from django.shortcuts import redirect
from django.urls import path, include

app_name = 'article'
urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_details, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    # path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    path(
        'article-safe-delete/<int:id>/',
        views.article_safe_delete,
        name='article_safe_delete'
    ),
    path('article-update/<int:id>/', views.article_update, name='article_update'),
]
