'''employee serializer code is here'''
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    '''user serializer'''
    class Meta:
        '''user serializer meta'''
        model = User
        fields = '__all__'
