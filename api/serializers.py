from rest_framework import serializers
from api.models import CustomUser , Task
from rest_framework_simplejwt.tokens import RefreshToken , TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class EntitySerializer(serializers.HyperlinkedModelSerializer):
    Uid = serializers.ReadOnlyField()
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = [
            'Uid',
            'username',
            'email',
            'password'

        ]

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    Tid = serializers.ReadOnlyField()
    class Meta:
        model = Task
        fields = "__all__"


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad token')


            
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
    