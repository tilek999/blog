from django.shortcuts import render, HttpResponse
from .models import Article, Author, Comment
from django.contrib.auth.models import User
from .form import ArticleForm



def homepage(request):
    articles = Article.objects.all()
    return rendeArticler(request, "article/homepage.html",
     {"articles":articles}
     )

def authors(request):
    authors = Author.objects.all()
    return render(request, "article/authors.html",{"authors":authors})


def comment(request):
    comment = comment.objects.all()
    return render(request, "article/comment.html",{"comment":comment})


def users(request):
    context ={}
    context["users_all"] = User.objects.all()
    return render(request, "article/user.html",{"user":user})

def article(request ,id):
    # if request.method.method =="POST":
    #     article = Article.objects.get(id=id)
    #     article.active = False
    #     article.save() 
    #     return redirect(homepage)
    article = Article.objects.get(id=id)
    return render(request, "article/article.html",{"article":article})   

def add_article(request):
    if request.method == "POST":
        form = ArticleForm()
        article.title=request.POST.get('title')
        article.text=request.POST.get('text')
        authors = Article.objects.get(pk=author_id)
        print(authors)
        article.author = authors
        article.save()
    form = ArticleForm()
    return render(request, "article/add_article.html",{"form":form})

