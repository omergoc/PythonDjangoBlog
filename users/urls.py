from django.urls import path
from .views import loginUser, register, userLogout,index,writers

urlpatterns = [
    path('giris-yap/',loginUser, name="login"),
    path('kayit-ol/',register, name="register"),
    path('cikis-yap/',userLogout, name='logout'),
    path('yazarlar/',writers, name='writers'),
    path('writer/<slug:writers_slug>/', index, name="writers")
]
