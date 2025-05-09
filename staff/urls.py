from django.urls import path 
from .views import get_staff, get_staffs, delete_staff, update_staff






urlpatterns = [
    path('', get_staffs, name='staff-list'),
    path("<int:id>/", get_staff),
    path("<int:id>/", delete_staff),
    path("<int:id>/", update_staff)
]
