from rest_framework import serializers
from .models import *
class SignUpSerial(serializers.ModelSerializer):
    class Meta():
        model=CostumUser
        fields=('first_name','last_name','email','age','location','password')


class LogninSerial(serializers.ModelSerializer):
    class Meta():
        model=CostumUser
        fields=('username','password')

class PostSerializer(serializers.ModelSerializer):
    class Meta():
        model=Post
        fields=('__all__')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta():
        model=profile
        fields=('__all__')