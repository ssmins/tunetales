from django.shortcuts import render , redirect
from .models import Article 
from .forms import ArticleForm

# Create your views here.

def index(request): 
    # articles 의 첫 화면에서 , 어떤 정보를 보여줘야 하나 ? 
    # 1) static file - UI 구성을 위해 
    # 2) 당일 기준으로 인기순 정렬된 사연 + 노래들 
    articles = Article.objects.all() # filter 를 써야 할 것 ! 
    # 3) 마이페이지
    # 4) 사연 독려 버튼 

    context = { 
        'articles' : articles , 
    }
    return render(request, 'articles/index.html', context)  

def create(request): 
    # create 할 때 , 어떤 정보가 필요하고 어떤 과정으로 DB에 저장할 건가 ? 
    # form 을 활용해 얻을 수 있다. 
    if request.method == 'POST': 
        form = ArticleForm(request.POST) # POST 방식으로 들어온 요청을 할당 
        if form.is_valid(): 
            form.save() 
            return redirect('articles:index')
    else: 
        form = ArticleForm() 
    context = {
        'form' : form , 
    }
    return render(request, 'articles/create.html', context) 

def read(request, pk): 
    # read 할 때 , 어떤 정보가 필요한가 ? 
    article = Article.objects.get(pk=pk) 
    context = {
        'article' : article, 
    }
    return render(request, 'articles/read.html', context)  


def update(request, pk):  
    article = Article.objects.get(pk=pk) # 애초에 다루는 article 이 pk 값을 가진 것이기 때문에, context에는 pk가 들어갈 필요 없다. 
    if request.method == 'POST': 
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid(): 
            form.save() 
            return redirect('articles:read', article.pk) 
    else: 
        form = ArticleForm(instance=article) 
    context = { 
        'article' : article, 
        'form' : form , 
    }
    return render(request, 'articles/update.html', context) 
    

def delete(request, pk): 
    if request.method == 'POST': 
        article = Article.objects.get(pk=pk) 
        article.delete()
        return redirect('articles:index')
    else : 
        article = Article.objects.get(pk=pk) 
        return redirect('articles:read', article.pk) 