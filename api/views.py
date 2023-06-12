from django.shortcuts import render
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from api.models import CustomUser , Task
from api.serializers import EntitySerializer , TaskSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view , permission_classes 
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = EntitySerializer

    @action(detail=False , methods=['POST'])
    def signup(self, request , *arg , **kwargs):

        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception =True)

        email = serializer.validated_data['email']
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        print("USERNAME " + username)
        print("PASSWORD " + password)
        if CustomUser.objects.filter(username=username).exists():
            return Response({'message': 'A user with that username already EXIST.'}, status=status.HTTP_400_BAD_REQUEST)



        user = CustomUser.objects.create(username = username, email = email, password = make_password(password) )
        user.save

        return Response(
            {
                'Message': 'User Created Successfully',
                'status' : 200,
                'username':str(username),
                'email':str(email)
            }
        )
    @action(detail=True, methods=['get'])
    def task(self , request , pk = None):
        try:
            entity = CustomUser.objects.get(pk = pk)
            tsk = Task.objects.filter(user=entity)
            tsk_serializer = TaskSerializer(tsk, many=True, context = {'request': request})
            return Response(tsk_serializer.data)
        except Exception as e:
            return Response(
                {
                    'message' : str(e)
                }
            )


class LoginViewSet(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = authenticate(request, username=username, password=password)
            loggeduser = CustomUser.objects.get(username = username)
            
            if user is not None:
                login(request, user)
                return Response(
                    {'message': 'Logged In successfully ',
                    'status' : 200,
                    "Uid":         loggeduser.Uid
    })
            else:
                return Response({'error': 'Invalid credentials'}, status=400)
        except CustomUser.DoesNotExist:
            return Response(
                {
                    'message' : "username or passowrd is incorrect"
                }
            )

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response(
        {
            'user':str(request.user.username),
            'message':'Logged out successfully'
        }
    )
