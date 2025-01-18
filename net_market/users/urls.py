from django.urls import path

from .views import users, user_detail

urlpatterns = [
    path('users/', users),
    path('users/<int:id>', user_detail)
]