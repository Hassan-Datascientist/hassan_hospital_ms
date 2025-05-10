from django.urls import path
from .views import register_view, login_user

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_user, name='log-in')
]