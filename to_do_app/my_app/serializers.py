from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']

    def create(self,validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ToDo
        fields='__all__'

    # def validate(self,data):
    #     if data['TimeStamp']:
    #         raise serializers.ValidationError({'error' : "you cannot change the timestamp of ToDo"})
        # return data


