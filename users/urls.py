from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import UserDetail, UserList, UserTokenObtainPairView

urlpatterns = [
    path(
        "auth/login/",
        UserTokenObtainPairView.as_view(),
        name="login",
    ),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<str:lookup_id>/", UserDetail.as_view(), name="user-detail"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="refresh"),
]
