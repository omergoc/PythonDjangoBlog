from rest_framework.serializers import ModelSerializer,Serializer
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from users.models import Account

class UserSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields =  '__all__' 
    
"""
class AccountSerializer(ModelSerializer):
    account = UserSerializer()
    class Meta:
        model = Account
    
    def update(self, instance, validated_data):
        account = validated_data.pop('account')
        account_serializer = AccountSerializer(instance.account, data=account)
        account_serializer.is_valid(raise_exception=True)
        account_serializer.save()
        return super(UserSerializer, self).update(instance, validated_data)

"""

class ChangePasswordSerializer(Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
        
