'''employee views code is'''
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
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

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class GetUserToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})
