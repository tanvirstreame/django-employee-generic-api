'''employee views code is'''
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializers
from .models import User


class UserViewSet(generics.ListCreateAPIView):
    '''user create'''
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    '''user fetch'''
    queryset = User.objects.all()
    serializer_class = UserSerializers
