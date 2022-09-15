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
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def article_list(request):
    article_list  = ArticlePost.objects.all()
    paginator = Paginator(article_list, 10)
    
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {'articles': articles}
    return render(request, 'article/list.html', context)
    # return HttpResponse("Hello World!")


def article_details(request, id):
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(article.body,
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        ])
    context = { 'article': article }
    return render(request, 'article/detail.html', context)

def article_create(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=1)
            new_article.save()
            return redirect("article:article_list")
        else:
            return HttpResponse("ERROR:article_create code 1")
    # 如果用户请求获取数据
    elif request.method == "GET":
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'article/create.html', context)


# def article_delete(request, id):
#     ArticlePost.objects.get(id=id).delete()
#     return redirect("article:article_list")

def article_safe_delete(request, id):
    if request.method == 'POST':
        ArticlePost.objects.get(id=id).delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("error: POST only.")

@login_required(login_url='/userprofile/login/')
def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect("article:article_detail", id=id)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    else:
        article_post_form = ArticlePostForm()
        context = {'article': article, 'article_post_form': article_post_form}
        return render(request, 'article/update.html', context)
