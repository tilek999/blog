from django.shortcuts import render, HttpResponse, redirect
from .form import ArticleForm, AuthorForm
from .models import Article, Author, Comment
from django.contrib.auth.models import User




def homepage(request):
    articles = Article.objects.all()
    return render(request, "article/homepage.html", {"articles":articles})

def author(request):
    authors = Author.objects.all()
    return render(request, "article/authors.html",{"authors":authors})

def profile(request, pk):
    profiles = Author.objects.get(id=pk)
    return render(request, "article/profile.html",{"profiles":profiles})


def comment(request):
    comment = Comment.objects.all()
    return render(request, "article/comment.html",{"comment":comment})


def users(request):
    context ={}
    context["users_all"] = User.objects.all()
    return render(request, "article/user.html",{"users":users})

def article(request ,id):
    if request.method =="POST":
        article = Article.objects.get(id=id)
        article.active = False
        article.save()
        return redirect(homepage)
    article = Article.objects.get(id=id)
    return render(request, "article/article.html", {'article': article})


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(homepage)
    form = ArticleForm()
    return render(request, "article/add_article.html",{"form":form})
       # form = ArticleForm()
       # article.title=request.POST.get('title')
      #  article.text=request.POST.get('text')
       # author_id = request.POST.get('author')
      #  authors = Article.objects.get(id=author_id)
       # article.author = authors
       # article.save()
    #form = ArticleForm()
   


def add_author(request):
    if request.method == "GET":    
        form = AuthorForm()
        context = {}
        context["form"] = form
        return render(request, "article/add_author.html",{"form":form})
    elif request.method == "POST":
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
     #   name = request.POST.get("name")  
      #  user_id = request.POST.get("user")
       # user = user.objects.get(id=user_id)
       # author = Author(name=name, user=user) 
       # author.save()
        return render(request, "article/add_author.html",{"form":form})
        

def edit_article (request, id):
    article = Article.objects.get(id=id)
    form = ArticleForm(instance=article)
    return render(request,  "article/add_article.html",{"form":form})
