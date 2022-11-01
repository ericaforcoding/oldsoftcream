from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save() 
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
    'article_form': article_form
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Articles.objects.get(pk=pk)
    form = CommentForm()
    context = {
        'article': article, 
        'form': form,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Articles.objects.get(pk=pk)
    if request.method == 'POST':
        article_form  = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    article = Articles.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')