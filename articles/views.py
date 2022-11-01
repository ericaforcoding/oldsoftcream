from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def create(request):
    pass

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


    