from django.contrib.auth import get_user_model
from rest_framework import serializers
from Users.models import CustomUser
from django.contrib.auth.models import Group, Permission

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name')

class RegisterSerializer(serializers.ModelSerializer):
    
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
    )
    
    password = serializers.CharField(write_only=True)
    Role = serializers.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['email', 'password','username', 'first_name', 'last_name','Role']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        Role = validated_data.get('Role')
        
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            Role = validated_data.get('Role') )
        # Assign the user to the chosen role (group)
        if Role == 'buyer':
            group = Group.objects.get(name='Buyers')
        elif Role == 'seller':
            group = Group.objects.get(name='Sellers')
        elif Role == 'admin':
            group = Group.objects.get(name='Admins')
        
        user.groups.add(group)
        
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

