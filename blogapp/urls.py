"""blogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views


handler404 = 'pages.views.handler404'

urlpatterns = [
    path('portal_fa956b808c8f8e3b59be14d7d584761e041a8359d58ba7e1829f12605d76203a/', admin.site.urls),
    path('api/user/',  include('users.api.urls'), name='account'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
    path('', include('pages.urls')),
    path('', include('articles.urls')),
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

handler404 = 'pages.views.not_found_404'

