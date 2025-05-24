from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
#from .filters import ProductFilter  
from .models import *
from .serializers import *
from django.contrib.auth.hashers import make_password
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def sign_up(request):
    data=request.data
    user=SignUpSerial(data = data)


    if user.is_valid():
       if not CostumUser.objects.filter(username=data['email']).exists():
           user =CostumUser.objects.create(
               first_name=data['first_name'],
               last_name=data['last_name'],
               email=data['email'],
               username=data['email'],
               age=data['age'],
               location=data['location'],
               password=make_password(data['password'])
           ) 
           return Response({'User':'is regestered'},status=status.HTTP_201_CREATED)
       else:    
           return Response({'User':'is already exists'},status=status.HTTP_400_BAD_REQUEST)
    else:
         return Response({'error':'user error'})


@api_view(['POST'])
def log_in(request):
    data=request.data
    serializers=LogninSerial(data=data)
    if CostumUser.objects.filter(username=data['username']).exists():
        user=CostumUser.objects.get(username=data['username'])
        if user.password==data['password']:
            return Response({"done":"is currect"})
        else:
            return Response({"error":"wrong password"})
    else:
        return Response({"error":"user not found"})
    
@api_view(['POST']) 
@permission_classes([IsAuthenticated]) 
def create_post(request):
    try:
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save(user=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    


