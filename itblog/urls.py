"""itblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from article.views import article, author, comment, homepage,profile, add_author, add_article, users,edit_article, add_comment, edit_comment,delete_comment
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",homepage, name="homepage"),
    path('profile/<int:pk>/',profile, name="profile"),
    path('author/', author, name= 'authors'),
    path("users/",users, name="users-list"),
    path("article/<int:id>/", article, name="article"),
    path("comment/<int:id>/",comment, name="comment" ),
    path("article/edit/<int:id>/", edit_article, name="edit-article"),
    path("article/add/", add_article, name = "add_article"),
    path("author/add/",add_author,name = "add_author"),
    path("comment/add/",add_comment,name="add_comment"),
    path("comment/<int:id>/edit/",edit_comment,name="edit_comment"),
    path("comment/<int:id>/delete/",delete_comment,name="delete_comment")
]   
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
