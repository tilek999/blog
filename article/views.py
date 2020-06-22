from django.shortcuts import render, HttpResponse, redirect
from article.form import ArticleForm, AuthorForm, CommentForm
from article.models import Article, Author, Comment
from django.contrib.auth.models import User




def homepage(request):
    

    if request.method == 'POST':
        key = request.POST.get('key_word')
        articles = Article.objects.filter(active=True).filter(
            title__contains=key) | Article.objects.filter(active=True).filter(
                text__contains = key)| Article.objects.filter(active=True).filter(tag__name__contains = key)
    else:
        articles = Article.objects.filter(active=True).order_by("likes")

    return render(request, "article/homepage.html", {"articles":articles})

def author(request):
    authors = Author.objects.all()
    return render(request, "article/authors.html",{"authors":authors})

def profile(request, pk):
    profiles = Author.objects.get(id=pk)
    return render(request, "article/profile.html",{"profiles":profiles})

def comment(request):
    comment = Comment.objects.get
    return render(request, "article/article.html",{"comment":comment})

def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(homepage)


def edit_comment(request, id):
    comment=Comment.objects.get(id=id)
    if request.method == "POST":
        form=CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()   
    form = CommentForm(instance=comment)
    return render(request,"article/comment",{"form":form})

def delete_comment(request, id):
    Comment.objects.get(id=id).delete()
    return render(request, "article/homepage.html")

def users(request):
    context ={}
    context["users_all"] = User.objects.all()
    return render(request, "article/user.html",{"users":users})

def article(request ,id):
    article = Article.objects.get(id=id)
    article.views +=1
    user = request.user
    if not user.is_anonymous:
        article.readers.add(user)
    article.save()
    if request.method =="POST":
        article = Article.objects.get(id=id)
        article.active = False
        article.save()
        return redirect(homepage)
    elif "comment_btn" in request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=comment(user=user,
            article=article,
            text=form.cleaned_data["text"])
            comment.save()
            return redirect(homepage)
    return render(request, "article/article.html", {'article': article})


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(homepage)
    form = ArticleForm()
    return render(request, "article/add_article.html",{"form":form})
   


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
        return render(request, "article/add_author.html",{"form":form})
        

def edit_article (request, id):
    article = Article.objects.get(id=id)
    form = ArticleForm(request.FILES, instance=article)
    return render(request,  "article/add_article.html",{"form":form})
