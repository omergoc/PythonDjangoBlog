from django.urls import path
from .views import index,contact,brand,about, trend, services,favorites,robots_txt

urlpatterns = [
    path('', index, name="index"),
    path('iletisim/',contact, name="contact"),
    path('markalar/',brand, name="brand"),
    path('hakkimizda/',about, name="about"),
    path("trend/", trend, name="trend"),
    path("favorites/", favorites, name="favorites"),
    path("hizmetler/", services, name="services"),
    path("robots.txt", robots_txt),

]
