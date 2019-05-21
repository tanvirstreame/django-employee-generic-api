'''employee views code is'''
from rest_framework import generics
from .serializers import UserSerializers
from .models import User


class UserViewSet(generics.ListCreateAPIView):
    '''user create'''
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    '''user fetch'''
    queryset = User.objects.all()
    serializer_class = UserSerializers
