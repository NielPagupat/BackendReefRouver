from django.contrib.auth import get_user_model
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, ActivationSerializer
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from .models import CustomUser
from djoser import utils
User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):

    confirm_password = serializers.CharField(max_length = 255, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password', 'first_name', 
                  'last_name', 'address', 'organization_name', 'contact_info', 'user_class']
    
    def validate(self, attrs):
        confirm_password = attrs.get('confirm_password')
        attrs.pop('confirm_password')
        user = User(**attrs)
        password = attrs.get('password')
        if confirm_password != password:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        try:
                validate_password(password, self.instance)
        except DjangoValidationError as e:
            raise serializers.ValidationError({'password': str(e)})

        print(attrs)
        return attrs
        

class GetUserInfo(serializers.ModelSerializer):
     class Meta:  
          model = CustomUser
          fields = ["password",
                    "last_login",
                    "date_joined",
                    "email",
                    "first_name",
                    "last_name",
                    "address",
                    'organization_name', 
                    'contact_info',]
          
