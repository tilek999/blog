from django.shortcuts import render, HttpResponse, redirect
from article.form import ArticleForm, AuthorForm, CommentForm
from article.models import Article, Author, Comment
from django.contrib.auth.models import User
from django.db.models import Q




def homepage(request):
    if request.method == 'POST':
        key = request.GET.get('key_word')
        article = Article.objects.filter(Q(active=True), Q(title__contains=key) 
            | Q(text__contains=key) | Q(tag__name__contains=key) 
                | Q(reader__username__contains=key) | Q(comment__text__contains=key) | Q(picture__name__contains=key))
        articles = articles.objects.distinct()
    else:
        print(request.GET)
        if "key_word" in request.GET:
            articles = Article.objects.filter(active=True).filter(
            title__contains=key) | Article.objects.filter(active=True).filter(
                text__contains = key)| Article.objects.filter(active=True).filter(
                    tag__name__contains = key) |  Article.objects.filter(active=True).filter(
                    readers__username__contains = key) |  Article.objects.filter(active=True).filter(
                    comments__text__contains = key) |   Article.objects.filter(active=True).filter(
                    picture__name__contains = key )
            key = request.GET.get("key_word")
            
        articles = Article.objects.filter(active=True).order_by("likes")

    return render(request, "article/homepage.html", {"articles":articles})

def author(request):
    authors = Author.objects.all()
    return render(request, "article/authors.html",{"authors":authors})

def profile(request, pk):
    profiles = Author.objects.get(pk=pk)
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
    return render(request, "article/users_list.html",{"users":users})

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
            comment=comment(users=user,
            article=article,
            text=form.cleaned_data["text"])
            comment.save()
            return redirect(homepage)
    return render(request, "article/article.html", {'article': article})


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article()
            if not Author.objects.filter(user=request.user):
                author = Author(user=users, name = request.user.usernname)
                author.save()
            else:
                author = Author.objects.get(user=request.user)
            article = Article()
            article.author = author
            article.title = form.cleaned_data["title"]
            article.text = form.cleaned_data["text"]
            article.picture = form.cleaned_data["picture"]
            tags = form.cleaned_data["tags"]
            article.save()
            for tag in tags.split(","):
                obj, created = tag.objects.get_or_create(name=tag)
                article.tag.add(obj)
            article.save()
            return redirect("add_article")
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
