from django.shortcuts import render
from admin_app.models import Article,Category
from django.shortcuts import redirect

# Create your views here.
def index(request):
    articles = Article.objects.all()[:4]
    article_aleatoire = Article.objects.order_by('?').first()
    articles_populaires = Article.objects.order_by('counter')[:3]
    categories = Category.objects.all()

    context = {
        'article_aleatoire' : article_aleatoire,
        'categories': Category.objects.all(),
        'articles': Article.objects.all(),
        
    } 
    return render(request, 'index.html',context)

def articles(request):
    
    article_aleatoire = Article.objects.order_by('?').first()
    articles_populaires = Article.objects.order_by('counter')[:3]
    categories = Category.objects.all()

    catdata = request.GET
    cat = catdata.get('category')

    if cat is None:
        articles = Article.objects.all()
    else:
        articles = Article.objects.filter(category_id=cat)

    
    context = {
        'article_aleatoire' : article_aleatoire,
        'categories': Category.objects.all(),
        'articles': articles,
        
    }
    return render(request, 'articles.html', context)


def article_detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return redirect('articles')
    
    articles_similaires = Article.objects.filter(category=article.category).exclude(id=article_id)[:3]
    article.increment_counter()
    context = {
        'article_id': article_id,
        'article': article,
        'articles_similaires': articles_similaires,
    }
    
    return render(request, 'article_detail.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')