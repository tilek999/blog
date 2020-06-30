from django import forms
from article.models import Article, Author, Comment, Tag 


class ArticleForm(forms.ModelForm):
    tags = forms.CharField(max_length=255)
    class Meta:
        model = Article
        fields = ["title", "text", "picture", "tags", "tag"]

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "user"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]