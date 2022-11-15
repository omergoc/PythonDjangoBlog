from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ArticleSitemap
from rest_framework_simplejwt import views as jwt_views

sitemaps = {
    'blog':ArticleSitemap
}

handler404 = 'pages.views.handler404'
handler500 = 'pages.views.handler500'

admin.site.site_header = 'Siberatay Yönetim Paneli'
admin.site.site_title = 'Siberatay Panel'


urlpatterns = [
    path('portal_f4bf9f7fcbedaba0392f108c59d8f4a38b3838efb64877380171b54475c2ade8/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('api/user/',  include('users.api.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
    path('', include('pages.urls')),
    path('', include('articles.urls')),
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

