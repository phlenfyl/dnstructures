from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from dnstructure.settings import AUTH_USER_MODEL
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from ..models import *
from ..forms import *
users = get_user_model()

class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User created successfully'})
        else:
            return Response(serializer.errors)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        print(password)
        print(email)

        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            refresh = RefreshToken.for_user(user)  # Create refresh token
            print(str(refresh.access_token))
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'id': user.id,
                    'email': user.email,
                }
            })
        else:
            return Response({'error': 'Make sure your email and password are correct'})



@api_view(['POST'])
def signup(request):
    form = RegisterForm(request.POST)
    
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data.get('password1')
        print(password)
        
        user = User.objects.create_user(email=email, password1=password)
        user.save()
        return Response({'message': 'User created successfully'})
    else:
        email = request.data.get('email')
        password = request.data.get('password1')
        print(password)
        print(email)
        if email and password:
            user = User.objects.create_user(email=email, password1=password)
            user.save()
            return Response({'errors': 'other alternative'})
        return Response({'errors': 'nothing works'})


@api_view(['POST'])
def loggin(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'email': user.email,
            }
        })

    return Response({'error': 'Make sure your email and password are correct'})

@api_view(['POST'])
def reset_password(request):
    email = request.data.get('email')
    new_password = request.data.get('new_password')
    try:
        user = User.objects.get(email=email)
        user.set_password(new_password)
        user.save()
        return Response({'message': 'Password reset successfully'})
    except User.DoesNotExist:
        return Response({'error': 'User not found'})

@api_view(['POST'])
def logout(request):
    try:
        refresh_token = request.data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Successfully logged out"})
    except Exception as e:
        return Response({"error": str(e)})





