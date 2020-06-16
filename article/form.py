from django import forms
from article.models import Article, Author, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","text","author"]

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "user"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]