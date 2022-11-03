from django.shortcuts import render, redirect
from .models import Articles, Photo
from .models import Articles, Category, Comment

from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "articles/index.html")


def create(request):
    if request.method == "POST":
        article_forms = ArticleForm(request.POST, request.FILES)
        if article_forms.is_valid():
            article_form = article_forms.save(commit=False)
            article_form.user = request.user
            article_form.save()
            for img in request.FILES.getlist('imgs'):
                photo = Photo()
                photo.post = article_form
                photo.image = img
                photo.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/create.html", context)


def detail(request, pk):
    article = Articles.objects.get(pk=pk)
    form = CommentForm()
    context = {
        "article": article,
        "form": form,
    }
    return render(request, "articles/detail.html", context)


@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:detail", article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/update.html", context)


def delete(request, pk):
    article = Articles.objects.get(pk=pk)
    article.delete()
    return redirect("articles:index")


def category(request, category_pk):
    category = Category.objects.get(pk=category_pk)
    category_articles = Articles.objects.filter(category=category)
    context = {"category": category, "category_articles": category_articles}
    return render(request, "articles/category.html", context)

@login_required
def category_follow(request, category_pk):
    category = Category.objects.get(pk=category_pk)
    if request.user in category.category_followers.all():
        category.category_followers.remove(request.user)
        category_follow = False
    else:
        category.category_followers.add(request.user)
        category_follow = True
    return JsonResponse({'categoryFollow': category_follow, 'followCount': category.category_followers.count()})
    


@login_required
def like(request, pk):
    article = Articles.objects.get(pk=pk)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        is_liked = False
    else:
        article.like_users.add(request.user)
        is_liked = True
    return JsonResponse({"isLiked": is_liked, "likeCount": article.like_users.count()})


def comment(request, pk):
    article = Articles.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.articles = article
        comment.user = request.user
        comment.save()
        context = {
            "content": comment.content,
            "userName": comment.user.username,
            "userImgUrl": comment.user.profile.image.url,
            "created": comment.create_at,
        }
        return JsonResponse(context)
    return redirect("articles:detail", article.pk)


def comment_d(request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return redirect("articles:detail", comment.articles.pk)


def append(request):
    return render(request, "append.html")
