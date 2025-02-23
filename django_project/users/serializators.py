from rest_framework import serializers
from openpyxl import load_workbook
from .models import User


class UserSerializer(serializers.ModelSerializer):

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Возраст должен быть больше 18")
        return value

    class Meta:
        model = User
        # fields = ['name', 'age', 'email']
        fields = '__all__'

class NewSerializer(serializers.Serializer):
    login = serializers.CharField()
    email_str = serializers.EmailField()
    age = serializers.IntegerField()

class AuthSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField()

