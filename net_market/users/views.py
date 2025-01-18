import json

from django.http import JsonResponse
from django.shortcuts import render

from users.models import User

def users(request):
    if request.method == 'GET':
        users_rows = User.objects.all()
        users_data = users_rows.values('id', 'name', 'email', 'age', 'created_at', 'updated_at')
        return JsonResponse(list(users_data), safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        print(request.body)

        user = User.objects.create(
            name=data['name'],
            email=data['email'],
            age=data['age'],
        )
        return JsonResponse(
            {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'age': user.age,
                'created_at': user.created_at,
                'updated_at': user.updated_at,
            },
            status=201,
        )

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