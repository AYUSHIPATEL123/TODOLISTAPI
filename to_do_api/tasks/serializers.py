from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from tasks.tasks import send_email

class TaskSerializer(serializers.ModelSerializer):
    user_details = serializers.ReadOnlyField(source='user.username')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model =  Task
        fields = '__all__'
        read_only_fields = ['user']
        required = ['title','discription','status','user','user_details']
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']
        extra_kwargs = {'password':{'write_only':True}}

    def validate(self,data):
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('User with this email already exists')
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('User with this username already exists')
        return data
    def validate_password(self,value):
        if len(value)<8:
            raise serializers.ValidationError('Password must be at least 8 characters long')
        return value
    
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        # user.set_password(validated_data['password'])
        if not user:
            raise serializers.ValidationError('User could not be created, try again')
        user.save()
        send_email.delay(user.pk)
        return user
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
             