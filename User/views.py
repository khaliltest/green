from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegestrationSerializers
from rest_framework.authtoken.models import Token



@api_view(['POST',])
def OwnerRegister(request):
    if request.method == 'POST':
        serializer = RegestrationSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            account  = serializer.save()
            data['response'] = "register successfully done"
            data['email'] = account.email
            data['username'] = account.username
            data['is_advisor'] = False
            data['is_owner'] = True
            data['number'] = account.number
            data['code_agency'] = account.code_agency
            data['full_name'] = account.full_name
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST',])
def AdvisorRegister(request):

    if request.method == 'POST':
        serializer = RegestrationSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            account  = serializer.save()
            data['response'] = "register successfully done"
            data['email'] = account.email
            data['username'] = account.username
            data['is_advisor'] = True
            data['is_owner'] = False
            data['number'] = account.number
            data['code_agency'] = account.code_agency
            data['full_name'] = account.full_name
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


@api_view(['POST',])
def UserRegister(request):

    if request.method == 'POST':
        serializer = RegestrationSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            account  = serializer.save()
            data['response'] = "register successfully done"
            data['email'] = account.email
            data['username'] = account.username
            data['is_advisor'] = False
            data['is_owner'] = False
            data['number'] = account.number
            data['code_agency'] = account.code_agency
            data['full_name'] = account.full_name
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)





