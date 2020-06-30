from django.db import models
from django.contrib.auth.models import User
from django.db import models 
from django.db.models import Model 
from datetime import datetime
# Create your models here. 

class Author(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="author_photo", null=True, blank=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="author",
    null=True, blank=True
    )
    def __str__(self):
        return self.name
    
    class Meta:
            verbose_name = "автор"
            verbose_name_plural = "авторы"



class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    author = models.ForeignKey(
    to=Author, 
    on_delete=models.CASCADE,
    related_name="articles",
    null=True,
    blank=True
    )
    picture = models.ImageField(null=True,blank=True,upload_to="articles/" + str(datetime.today().strftime("%y%m%d")))
    dislikes = models.IntegerField(default=0) 
    views = models.IntegerField(default=0)
    reposts = models.IntegerField(default=0)
    tag = models.ManyToManyField("Tag", blank = True, related_name="article")
    publication_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    readers = models.ManyToManyField(to=User, related_name="articles",blank=True)

    class Meta:
            verbose_name = "артикл"
            verbose_name_plural = "артиклы"
            ordering = ['-publication_date']


    def __str__(self):
        return self.title

class Comment(models.Model):
        text=models.TextField(null=True, blank=True)
        Article = models.ForeignKey(to=Article, on_delete=models.CASCADE, related_name="Comment")  
        user= models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="Comment", null=True, blank=True)

        class Meta:
            verbose_name = "коментарий"
            verbose_name_plural = "коментарии"
            ordering = ["user"]


class Tag(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"