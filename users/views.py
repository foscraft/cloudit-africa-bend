from typing import Any

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, response, status
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from users.permissions import IsUser
from users.serializers import UserSerializer, UserTokenObtainPairSerializer

User = get_user_model()


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self) -> Any:
        return self.queryset.filter(is_active=True)

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUser]

    def get_object(self) -> Any:
        return get_object_or_404(
            self.get_queryset(), lookup_id=self.kwargs["lookup_id"]
        )


class UserTokenObtainPairView(TokenObtainPairView):  # type: ignore
    serializer_class = UserTokenObtainPairSerializer
    renderer_classes = (JSONRenderer,)
