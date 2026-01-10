from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.users.serializers import RegisterSerializer, CustonTokenSerializers

class AuthViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = RegisterSerializer

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        seralizer = CustonTokenSerializers(data=request.data)
        seralizer.is_valid(raise_exception=True)
        return Response(seralizer.validated_data)

        