from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from apps.users.serializers import (
    RegisterSerializer, CustonTokenSerializers,
    ResetPasswordConfirmSerializer, ResetPasswordSerializer
)

class AuthViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = RegisterSerializer

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        serializer = CustonTokenSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

    @action(detail=False, methods=['post'], url_path='reset-password', serializer_class=ResetPasswordSerializer)
    def reset_password(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "Ссылка для сброса пароля отправлена"},
            status=status.HTTP_200_OK
        )

 