from django import forms
from article.models import Article, Author


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","text","author"]

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "user"]
