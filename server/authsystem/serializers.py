from rest_framework import serializers

from .models import User, UserStatus


class StartPasswordRestoreSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PasswordRestoreSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class UserPresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", 'itn', 'username', 'email',)

class LoginRequestSerializer(serializers.ModelSerializer):
    '''Login serializer. Including name, surname, email, password, is_superuser, is_staff'''
    password = serializers.CharField(
        max_length=256
    )

    class Meta:
        model = User
        fields = ("email", 'password',)

class LoginSerializer(serializers.ModelSerializer):
    '''Login serializer. Including name, surname, email, password, is_superuser, is_staff'''
    id = serializers.UUIDField()
    password = serializers.CharField(
        max_length=256
    )
    itn = serializers.IntegerField()

    class Meta:
        model = User
        fields = ("__all__")
    
    def validate_ratio(self, itn):
         try:
             return int(itn)
         except ValueError:
            raise serializers.ValidationError('Valid integer is required')
         
class RegisterSerializer(serializers.ModelSerializer):
    '''Register serializer. Including name, surname, email, password, is_superuser, is_staff'''
    password = serializers.CharField(
        max_length=256
    )

    
    class Meta:
        model = User
        fields = ("__all__")

    
    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(**validated_data,)

class UserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatus
        fields = ("title",)

    

class UserPatchingSerializer(serializers.ModelSerializer):
    '''Serializer for user patching. Including name, surname, email, password, is_superuser, is_staff'''
    class Meta:
        model = User
        fields = ("__all__")