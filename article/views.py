from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import ArticlePost
import markdown
from django.shortcuts import render, redirect
# 引入HttpResponse
# 引入刚才定义的ArticlePostForm表单类
from .forms import ArticlePostForm
# 引入User模型
from django.contrib.auth.models import User


def article_list(request):
    articles = ArticlePost.objects.all()
    if len(articles) >= 100:
        articles = articles[:99] + "..."
    context = {'articles': articles}
    return render(request, 'article/list.html', context)
    # return HttpResponse("Hello World!")


def article_details(request, id):
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(
        article.body,
        extensions=[
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
        ])
    context = {'article': article}
    return render(request, 'article/detail.html', context)


def article_create(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new = article_post_form.save(commit=False)
            new.author = User.objects.get(id=1)
            new.save()
            return redirect("article:article_list")
        else:
            return HttpResponse("error:form content")
    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'article/create.html', context)
