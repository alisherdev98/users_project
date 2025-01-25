import json
import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.exceptions import ValidationError

from users.models import User
from .serializators import UserSerializer, NewSerializer

def users(request):
    if request.method == 'GET':
        users_rows = User.objects.all()
        users_data = users_rows.values('id', 'name', 'email', 'age', 'created_at', 'updated_at', 'phone')
        return JsonResponse(list(users_data), safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        print(request.body)

        errors = {}

        if not isinstance(data['age'], int):
            errors['age'] = 'Возраст должен быть целым числом'
        if data.get('phone') is None:
            errors['phone'] = 'Телефон обязателен'

        if errors:
            raise JsonResponse(errors, status=400)

        user = User.objects.create(
            name=data['name'],
            email=data['email'],
            age=data['age'],
            phone=data['phone'],
        )
        return JsonResponse(
            {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'age': user.age,
                'created_at': user.created_at,
                'updated_at': user.updated_at,
                'phone': user.phone,
            },
            status=201,
        )


def users2(request):
    if request.method == 'GET':
        users_rows = User.objects.all()
        serializer = UserSerializer(users_rows, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = UserSerializer(data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def user_detail(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    if request.method == 'GET':
        return JsonResponse(
            {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'age': user.age,
                'created_at': user.created_at,
                'updated_at': user.updated_at,
                'phone': user.phone
            },
            status=200,
        )
    elif request.method == 'PUT':
        data = json.loads(request.body)
        user.name = data['name']
        user.email = data['email']
        user.age = data['age']
        user.save()
        return JsonResponse(
            {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'age': user.age,
                'created_at': user.created_at,
                'updated_at': user.updated_at,
            },
            status=200,
        )
    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({}, status=204)

def user_detail2(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({}, status=204)


def user_test(request):
    data = json.loads(request.body)

    serializer = NewSerializer(data=data)

    if serializer.is_valid():

        return JsonResponse(serializer.validated_data)
    return JsonResponse(serializer.errors, status=400)