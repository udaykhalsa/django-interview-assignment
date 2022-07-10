from rest_framework import serializers
from .models import User


USER_ROLE = (
    ('librarian', 'Librarian'),
    ('member', 'Member')
)

class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    name = serializers.CharField()
    role = serializers.ChoiceField(choices=USER_ROLE, required=False)
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        try:
            user = User.objects.get(username=username)
        except:
            user = None

        if user:
            raise serializers.ValidationError('User with given username already exists.')

        if password != confirm_password:
            raise serializers.ValidationError('Passwords do not match.')

        return data


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            user = None
        
        if not user:
            raise serializers.ValidationError('User with given username does not exists.')

        if not user.is_active:
            raise serializers.ValidationError('User account is not active.')

        if not user.check_password(password):
            raise serializers.ValidationError('Incorrect password.')

        return data

class UserDeactivateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    def validate(self, data):
        user_id = data.get('user_id')

        try:
            user = User.objects.get(id=user_id)
        except:
            user = None

        if not user:
            raise serializers.ValidationError('User with given ID does not exists.')
    
        if not user.is_active:
            raise serializers.ValidationError('User is already deactivated.')

        return data


class MemberSerializer(serializers.ModelField):
    class Meta:
        model = User
        fields = '__all__'


