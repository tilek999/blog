from django.db import models
from django.contrib.auth.models import User
from django.db import models 
from django.db.models import Model 
# Create your models here. 

 



class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    author = models.ForeignKey(
    to="Author", 
    on_delete=models.CASCADE,
    related_name="articles",
    null=True,
    blank=True
    )
    readers = models.ManyToManyField(to=User, related_name="articles",blank=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
        text=models.TextField(null=True, blank=True)
        Article = models.ForeignKey(to=Article, on_delete=models.CASCADE, related_name="Comment")  
        user= models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="Comment", null=True, blank=True)




class Author(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="author_photo", null=True, blank=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="author",
    null=True, blank=True
    )
    def __str__(self):
        return self.name