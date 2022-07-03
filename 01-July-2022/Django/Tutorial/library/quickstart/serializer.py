from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):

    class Mets:
        model = Todo
        fields = '__all__'