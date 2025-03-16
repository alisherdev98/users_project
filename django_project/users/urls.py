from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.olds import  user_detail, users2, user_detail2, user_test, User4, User5, UserDetail5, User3, UserDetail3
from .views.news import UserViewSet
from .views.olds import auth, logout_view

router = DefaultRouter()
router.register('v6/users', UserViewSet)


urlpatterns = [
    # path('users/', users),

    path('auth/', auth),
    path('logout/', logout_view),

    path('users/<int:id>', user_detail),

    path('users2/', users2),
    path('users2/<int:id>', user_detail2),
    path('test/', user_test),
    path('users4/', User4.as_view()),

    path('v3/users/', User3.as_view()),
    path('v3/users/<int:pk>', UserDetail3.as_view()),

    path('v5/users/', User5.as_view()),
    path('v5/users/<int:pk>', UserDetail5.as_view()),


]

urlpatterns += router.urls


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Получение токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Обновление токена
]