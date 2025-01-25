from django.urls import path

from .views import users, user_detail, users2, user_detail2, user_test

urlpatterns = [
    path('users/', users),
    path('users/<int:id>', user_detail),
    path('users2/', users2),
    path('users2/<int:id>', user_detail2),
    path('test/', user_test),
]