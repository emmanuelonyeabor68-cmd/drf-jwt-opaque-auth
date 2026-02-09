from django.shortcuts import render
from datetime import timedelta
from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .throttles import LoginRateThrottle
from .throttles import RefreshRateThrottle


from .models import RefreshToken

# Create your views here.

class LoginView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [LoginRateThrottle]

    def post(self, request):
        user = authenticate(

        username = request.data.get("username"),
        password = request.data.get("password") ) 
            
        #user = authenticate(username=username,password=password)

             

        if not user:
            return Response({
                "message": "Invalid credentials"
            }, 
            status=status.HTTP_401_UNAUTHORIZED)
        
        access = AccessToken.for_user(user)
        refresh = RefreshToken.objects.create(
            user=user,
            token=RefreshToken.generate(),
            expires_at=timezone.now() + timedelta(days=7)
        )
        
        return Response({
            "access": str(access),
            "refresh": refresh.token
        },
        status=status.HTTP_200_OK)
        
            


class RefreshView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [RefreshRateThrottle]

    def post(self, request):
        token = request.data.get("refresh")
        
        try:
            refresh = RefreshToken.objects.get(token=token)
        except RefreshToken.DoesNotExist:
            return Response({
                "message": "invalid refresh token"
            },
            status=status.HTTP_401_UNAUTHORIZED)
        
        if not refresh.is_valid():
            return Response({
                "message": "Token reuse detected. Expired or revoked"
            },
            status=status.HTTP_401_UNAUTHORIZED)
        
        #if refresh.revoked:
         #   RefreshToken.objects.filter(user=refresh.user).update(revoked=True)
          #  return Response(
           #     {"message": "Token reuse detected. Please logon again"},
            #status=status.HTTP_401_UNAUTHORIZED    
        #    )
        
        refresh.revoked = True
        refresh.save()

        new_refresh = RefreshToken.objects.create(
            user=refresh.user,
            token=RefreshToken.generate(),
            expires_at=timezone.now() + timedelta(days=7)

        )

        new_access = AccessToken.for_user(refresh.user)

        return Response({
            "access": str(new_access),
            "refresh": new_refresh.token
        })
    
class LogoutView(APIView):
    def post(self, request): 
        refresh_Token = request.data.get("refresh")

        if not refresh_Token:
            return Response(
                {"detail": "Refresh token required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            token = RefreshToken.objects.get(token=refresh_Token)
            token.delete()

            return Response(
                {"detail": "logged out successfully"},
                status=status.HTTP_200_OK
            )  
        except RefreshToken.DoesNotExist:
            return Response(
                {"detail": "Invalid refresh token"},
                status=status.HTTP_400_BAD_REQUEST
            ) 
               


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(requests):
    return Response({
        "message": f"Hello {requests.user.username}, you are authenticated"
    })
