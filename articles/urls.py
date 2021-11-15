from django.urls import path
from . import views

urlpatterns = [
    path('<slug:categories_slug>/', views.category, name="category"),
    path('<slug:categories_slug>/<slug:articles_slug>/', views.article, name="article"),
]
