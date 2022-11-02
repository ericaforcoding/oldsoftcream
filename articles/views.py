from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form,
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

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    if request.method == 'POST':
        article_form  = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form,
    }
    return render(request, 'articles/update.html', context)


def delete(request, pk):
    article = Articles.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def category(request):
    category = request.GET.get('category')
    category_articles = Articles.objects.filter(category=category)
    context = {'category' : category, 'category_articles' : category_articles}
    return render(request, 'articles/category.html', context)

def user_page(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    articles = Articles.objects.filter(user=user)
    context = {'user': user, 'articles': articles}
    return render(request, 'articles/user_page.html', context)


