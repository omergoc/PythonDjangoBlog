from django.urls import path
from users.api.views import (
    AccountView,
    UpdatePassowrd
)

app_name = 'users'

urlpatterns = [
    path('me', AccountView.as_view(), name='me'),
    path('change-password', UpdatePassowrd.as_view(), name='change-password')
]
