from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# Create your views here.

# Authentication of the user is done here
class RegisterUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 200, 'message': 'Wrong Credentials!!'})
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        token_obj,_=Token.objects.get_or_create(user=user)

        return Response({
            'status':200,
            'payload':serializers.data,
            'token':str(token_obj),
            'message':'Your credentials are saved!'}
        )

# this APIView contains all the necessary APIS to test our App
class ToDoAPI(APIView):

    #Authentication is checked here
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        try:
            id=request.query_params['id']
            if id!=None:
                item = ToDo.objects.get(id=id)
                serializers = ToDoSerializer(item)
        except:
            ToDos = ToDo.objects.all()
            serializers = ToDoSerializer(ToDos, many=True)
            # return Response({'status': 200, 'payload': serializers.data})
        return Response({'status': 200, 'payload': serializers.data})

    def post(self,request):
        data=request.data
        serializer=ToDoSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status': 200, 'message': 'Wrong data!!'})
        serializer.save()
        return Response({'status':200,'payload':data,'message':'Your data is saved!'})

    def put(self,request):
        try:
            todo_obj = ToDo.objects.get(id=request.data['id'])
            serializer = ToDoSerializer(todo_obj, data=request.data,partial=True)

            if not serializer.is_valid():
                print(serializer.errors())
                return Response({'status': 403, 'message': 'holona aar ki kora jabe!'})

            serializer.save()
            return Response({'status': 200, 'message': 'data updated!'})
        except Exception as e:
            return Response({'status': 403, 'message': 'invalid id'})

    def delete(self,request):
        try:
            todo_obj=ToDo.objects.get(id=request.query_params['id'])
            todo_obj.delete()
            return Response({'status': 200, 'message': 'data deleted!'})
        except Exception as e:
            return Response({'status': 403, 'message': 'invalid id'})















