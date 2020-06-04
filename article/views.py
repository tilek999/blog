from django.shortcuts import render, HttpResponse
from .models import Article,Author
import re

def homepage(request):
    articles=Article.objects.all()
    wind = Author.objects.get(id=1)
    return render(request, "article/homepage.html",
     {"articles":articles,"wind":wind}
     )

