from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.olds import users, user_detail, users2, user_detail2, user_test, User4, User5, UserDetail5
from .views.news import UserViewSet

router = DefaultRouter()
router.register('users6', UserViewSet)


urlpatterns = [
    path('users/', users),
    path('users/<int:id>', user_detail),
    path('users2/', users2),
    path('users2/<int:id>', user_detail2),
    path('test/', user_test),
    path('users4/', User4.as_view()),
    path('users5/', User5.as_view()),
    path('users5/<int:pk>', UserDetail5.as_view()),
]

urlpatterns += router.urls