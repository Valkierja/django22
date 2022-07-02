from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import ArirticlePost
def article_list(request):
    articles = ArirticlePost.objects.all()
    context = { 'articles' : articles }
    return render(request, 'article/list.html', context)
    #return HttpResponse("Hello World!")
