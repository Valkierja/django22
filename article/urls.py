import imp
from django.urls import path
from . import views
app_name = 'article'
urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_details, name='article_detail'),
]
