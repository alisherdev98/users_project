import xml.etree.ElementTree as ET
import json



def users2(request):
    if request.method == 'GET':
        users_rows = User.objects.all()
        serializer = UserSerializer(users_rows, many=True)
        return Response(serializer.data, safe=False)
    elif request.method == 'POST':

        if request.headers['content-type'] != 'application/json':

            data = json.loads(request.body)
        elif request.headers['content-type'] == 'application/xml':

            raw_str = request.body.decode('utf-8')

            root = ET.fromstring(raw_str)

            data = {}

            for child in root:
                data[child.tag] = child.text

        serializer = UserSerializer(data=json.loads(request.body))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)