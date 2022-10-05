from django.urls import path
from .views import loginUser, register, userLogout,index,users,profile,activate,userPasswordChange

urlpatterns = [
    path('giris-yap/',loginUser, name="login"),
    path('profil/',profile, name="profile"),
    path('kayit-ol/',register, name="register"),
    path('cikis-yap/',userLogout, name='logout'),
    path('password-change/',userPasswordChange, name='password_change'),
    path('uyeler/',users, name='users'),
    path('activate<uidb64>/<token>/', activate, name='activate'),  
    path('writer/<slug:writers_slug>/', index, name="writers")
]
