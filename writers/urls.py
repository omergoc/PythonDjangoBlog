from django.urls import path
from . import views

urlpatterns = [
    path('<slug:writers_slug>/', views.index, name="writers")
]
