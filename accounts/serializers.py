from rest_framework import serializers
from django.contrib.auth import get_user_model



User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', ]


