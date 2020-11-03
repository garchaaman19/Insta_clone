from django.contrib.auth.models import User,Group
from .models import Profile
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'



# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Profile
#         fields=[]
