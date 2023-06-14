from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from api.models import CustomUser , Task
from api.serializers import EntitySerializer , TaskSerializer , LogoutSerializer , CustomTokenObtainPairSerializer 
from rest_framework.response import Response
from rest_framework import viewsets , generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


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
                'Message': 'Signed Up Successfully',
                'status' : 200,
                'username':str(username),
                'email':str(email)
            }
        )

    @action(detail=False , methods=['POST'])
    def login(self, request ):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = authenticate(request , username=username , password = password)
            loggedUser = CustomUser.objects.get(username = username)

            if user is not None:
                login(request , user)
                custom_token = CustomTokenObtainPairView.serializer_class.get_token(user=user)
                print(custom_token)
                token = {
                    'refresh' : str(custom_token),
                    'access' : str(custom_token.access_token)
                }

                return Response(
                    {
                        'message' : 'Logged In successfully',
                        'status' : 200,
                        'Uid' : loggedUser.Uid,
                        'token' : token
                     }
                )
            else:
                return Response({'error': 'Invalid credentials'}, status=400)
        except CustomUser.DoesNotExist:
            return Response(
                {
                    'message' : "username or passowrd is incorrect"
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


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'status': 200,
            'message': 'Logged out successfully'
        }) 
    


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer





