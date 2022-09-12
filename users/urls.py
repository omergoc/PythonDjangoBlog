from django.urls import path
from .views import loginUser, register, userLogout,index,writers,profile

urlpatterns = [
    path('giris-yap/',loginUser, name="login"),
    path('profil/',profile, name="profile"),
    path('kayit-ol/',register, name="register"),
    path('cikis-yap/',userLogout, name='logout'),
    path('yazarlar/',writers, name='writers'),
    path('writer/<slug:writers_slug>/', index, name="writers")
]
