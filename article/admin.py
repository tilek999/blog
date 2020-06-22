from django.contrib import admin
from article.models import Article, Author, Comment, Tag


# Register your models here.
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Tag)
