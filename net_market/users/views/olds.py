import json


from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import JSONParser
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from django.http import HttpResponse
from openpyxl import load_workbook

from users.models import User
from users.serializators import UserSerializer, NewSerializer




class User2222:
    def get(self, request):
        ...
        # users_rows = User.objects.all()
        # users_data = users_rows.values('id', 'name', 'email', 'age', 'created_at', 'updated_at')
        # return JsonResponse(list(users_data), safe=False)

    def post(self, request):
        ...
        # if request.headers['content-type'] != 'application/json':
        #     data = json.loads(request.body)
        # elif request.headers['content-type'] == 'text/plain':
        #     print(request.body)
        #
        # errors = {}
        #
        # if not isinstance(data['age'], int):
        #     errors['age'] = 'Возраст должен быть целым числом'
        #
        # if errors:
        #     raise JsonResponse(errors, status=400)
        #
        # user = User.objects.create(
        #     name=data['name'],
        #     email=data['email'],
        #     age=data['age'],
        # )
        #
        # response_data = {
        #         'id': user.id,
        #         'name': user.name,
        #         'email': user.email,
        #         'age': user.age,
        #         'created_at': user.created_at,
        #         'updated_at': user.updated_at,
        #     }
        #
        # json_response_data = json.dumps(response_data)
        #
        # return HttpResponse(json_response_data
        #     ,
        #     status=201,
        # )

    @classmethod
    def as_view(cls):
        return cls()

    def __call__(self, request, *args, **kwargs):
        if request.method == 'GET':
            self.get(request)

        elif request.method == 'POST':
            self.post(request)

def users2(request):
    if request.method == 'GET':
        users_rows = User.objects.all()
        serializer = UserSerializer(users_rows, many=True)
        return Response(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = UserSerializer(data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class User3(APIView):

    parser_classes = [JSONParser, XMLParser]
    renderer_classes = [JSONRenderer, XMLRenderer]

    def get(self, request):
        users_rows = User.objects.all()
        serializer = UserSerializer(users_rows, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class User4(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class User5(ListCreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer




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


class UserDetail3(APIView):
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    def put(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

        serializer = UserSerializer(user, data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

        user.delete()
        return JsonResponse({}, status=204)



class UserDetail5(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer


class UserNewDetail(GenericAPIView, RetrieveModelMixin, DestroyModelMixin):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def get(self, request, id):
        return self.retrieve(request)

    def delete(self, request, id):
        return self.destroy(request)














def user_test(request):
    data = json.loads(request.body)

    serializer = NewSerializer(data=data)

    if serializer.is_valid():

        return JsonResponse(serializer.validated_data)
    return JsonResponse(serializer.errors, status=400)