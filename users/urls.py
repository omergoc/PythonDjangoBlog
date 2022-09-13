from django.urls import path
from .views import loginUser, register, userLogout,index,writers,profile,activate

urlpatterns = [
    path('giris-yap/',loginUser, name="login"),
    path('profil/',profile, name="profile"),
    path('kayit-ol/',register, name="register"),
    path('cikis-yap/',userLogout, name='logout'),
    path('yazarlar/',writers, name='writers'),
    path('activate<uidb64>/<token>/', activate, name='activate'),  
    path('writer/<slug:writers_slug>/', index, name="writers")
]
