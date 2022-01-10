import re

from django.contrib.auth.models import User
from rest_framework import serializers
from string import punctuation

from .models import (
    Banks,
    Student
)


# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     email = serializers.EmailField()
#     is_staff = serializers.BooleanField()
#     is_active = serializers.BooleanField()
#
#
# class UserSerializer2(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'is_staff', 'is_active']

class BanksSerializer(serializers.Serializer):
    n_of_or = serializers.CharField(max_length=100)
    op_dt = serializers.DateField()
    capital = serializers.CharField(max_length=100)
    ceo_of_cmp = serializers.CharField(max_length=100)
    ser_es = serializers.CharField(max_length=500)
    cards = serializers.CharField(max_length=300)
    n_of_br = serializers.IntegerField()
    n_of_emp = serializers.IntegerField()
    aff_com = serializers.CharField()


class BanksSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = [
            'id', 'n_of_or', 'op_dt', 'capital', 'ceo_of_cmp', 'ser_es', 'cards', 'n_of_br', 'n_of_emp', 'aff_com'
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            }
        }

    # def validate_password(self, password):
    #     if len(password) < 8:
    #         raise serializers.ValidationError({'password': "Password must be longer than 8 symbols"})
    #     psw = [1, 1, 1, 1]
    #
    #     return password


#  08/01/2022  #


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate_gpa(self, value):
        if not (0 < value <= 5):
            raise serializers.ValidationError({'gpa': "GPA must be between 0 and 5"})
        return value

    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError({'age': "Age must be greater then 0"})
        return value

    # def validate_password(self, value: str):
    #     if value <= 7:
    #         raise serializers.ValidationError({'password': "Password must be longer than 7 symbols"})
    #     return ('You entered ' + value)

# 10.01.2022 #


class StudentSerializer1(serializers.Serializer):
    firstname = serializers.CharField(max_length=30)
    secondname = serializers.CharField(max_length=30)
    language = serializers.CharField(max_length=30)
    course = serializers.CharField(max_length=30)
    gpa = serializers.FloatField()
    gender = serializers.CharField(max_length=30)
    age = serializers.IntegerField()


class StudentSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'firstname',
            'surname',
            'language',
            'course',
            'gpa',
            'gender',
            'age'
        ]

##


class UserSerializerMir(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    # def validate_password(self, value: str):
    #     if len(value) < 8:
    #         raise serializers.ValidationError('Password must be contain 8 symbols')
    #     result = [1, 1, 1, 1]
    #     for i in value:
    #         if i.isdigit():
    #             result[0] = 0
    #         elif i.islower():
    #             result[1] = 0
    #         elif i.isupper():
    #             result[2] = 0
    #         elif i in punctuation:
    #             result[3] = 0
    #     if result[0]:
    #         raise serializers.ValidationError('password must contain digits')
    #     elif result[1]:
    #         raise serializers.ValidationError('password must contain at least one lowercase latter')
    #     elif result[2]:
    #         raise serializers.ValidationError('password must contain at least one uppercase latter')
    #     elif result[3]:
    #         raise serializers.ValidationError('password must contain at least one punctuation latter')
    #
    #     return value

    def validate_password(self, value: str):
        length_error = len(value) < 8
        digit_error = re.search(r"\d", value) is None
        uppercase_error = re.search(r"[A-Z]", value) is None
        lowercase_error = re.search(r"[a-z]", value) is None
        symbol_error = re.search(r"[ !£$%&'()*+,-/[\\\]^_{~}" + r'"]', value) is None

        if length_error:
            raise serializers.ValidationError('Password nmust contain 8 symbols')
        elif digit_error:
            raise serializers.ValidationError('Password must contain digits')
        elif lowercase_error:
            raise serializers.ValidationError('Password must contain at least lowercase latter')
        elif uppercase_error:
            raise serializers.ValidationError('Password must contain at least uppercase latter')
        elif symbol_error:
            raise serializers.ValidationError('Password must contain at least one punctuation latter')

        return value

