from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views


handler404 = 'pages.views.handler404'
handler500 = 'pages.views.handler500'

admin.site.site_header = 'Siberatay Yönetim Paneli'
admin.site.site_title = 'Siberatay Panel'


urlpatterns = [
    path('portal_fa956b808c8f8e3b59be14d7d584761e041a8359d58ba7e1829f12605d76203a/', admin.site.urls),
    path('api/user/',  include('users.api.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
    path('', include('pages.urls')),
    path('', include('articles.urls')),
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

