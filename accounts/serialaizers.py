from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, validators=[validate_password])


    class Meta:
        model = User
        fields = ['username','email','password']

    def validate_email(self, value):
            if User.objects.filter(email__iexact=value).exists():
                raise serializers.ValidationError('email алакай вучуд дорад')
            return value.lower()
    

class Userserialazer(serializers.BaseSerializer):
    class Meta:
        madel = User
        fields = ['username','email','date_joined', 'last_login']

        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer): 
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token        
        
        
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def save(self, **kwargs):
        try:
            RefreshToken(self.validated_data['refresh']).blacklist()
        except TokenError:
            raise serializers.ValidationError({'refresh': 'Token is invalid or expired.'}) 


    

    

    




















   



        