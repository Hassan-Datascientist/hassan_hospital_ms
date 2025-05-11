from django.urls import path
from .views import register_view, login_user, logout_user, home

urlpatterns = [
    path('', home, name="home"),
    path('register/', register_view, name='register'),
    path('login/', login_user, name='log-in'),
    path('logout/', logout_user, name='log-out')
]