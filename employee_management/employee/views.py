'''employee views code is'''
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import pagination
from .serializers import EmployeeSerializers, UserSerializer
from .models import Employee




class EmployeeDetailPaginationView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class UserCreate(generics.ListCreateAPIView):
    '''user fetch'''
    serializer_class = UserSerializer


class EmployeeViewSet(generics.ListCreateAPIView):
    '''user create'''
    permission_classes = (IsAuthenticated,)

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    '''user fetch'''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
