from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.article_comment, name="article_comment"),
    path('like/', views.article_like, name="article_like"),
    path('videolar/', views.videos, name="videos"),
    path('haberler/', views.news, name="news"),
    path('makaleler/', views.articles, name="articles"),
    path('<slug:categories_slug>/', views.category, name="category"),
    path('<slug:categories_slug>/<slug:articles_slug>/', views.article, name="article"),
]
