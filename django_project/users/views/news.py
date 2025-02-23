import json

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from users.models import User
from users.serializators import UserSerializer

# from users.serializators import AuthSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=204)






class TokenGenerator(APIView):
    def post(self, request):
        data = json.load(request.body)

        serializer = AuthSerializer(data=data)
        if serializer.is_valid():
            token = serializer.validated_data['login'][-3:] + serializer.validated_data['password'][-3:]
            return Response({'token': token})

        return Response(serializer.errors, status=400)