from django.urls import path
from .views import index,contact,brand,about, trend, services,favorites, PostJsonListView

urlpatterns = [
    path('', index, name="index"),
    path('posts_json/<int:id>/', PostJsonListView, name="posts_json"),
    path('iletisim/',contact, name="contact"),
    path('markalar/',brand, name="brand"),
    path('hakkimizda/',about, name="about"),
    path("trend/", trend, name="trend"),
    path("favorites/", favorites, name="favorites"),
    path("hizmetler/", services, name="services")
]
