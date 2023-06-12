from rest_framework import serializers
from api.models import CustomUser , Task

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