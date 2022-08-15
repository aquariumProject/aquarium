from members.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

#회원가입 시리얼라이저
class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    nickname=serializers.CharField(
        write_only=True,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password=serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'},
    )
    password2=serializers.CharField(write_only=True,required=True,style={'input_type': 'password'})

    class Meta:
        model=User
        fields=('username','password','password2','email','nickname')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return data

    def create(self,validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            nickname=validated_data['nickname'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token= Token.objects.create(user=user)
        return user
    

# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True, write_only=True, style={'input_type': 'password'},)

    def validate(self, data):
        user = authenticate(**data)
        print("validate user")
        print(user)
        if user:
            # username = Token.objects.get(username=username)
            # password = Token.objects.get(password=password)
            token = Token.objects.get(user=user)
            print("views token")
            print(token)
            return token
            # userdata = {"user" : user}
            # return userdata
        
        raise serializers.ValidationError(
            {"error": "Wrong access"}
        )