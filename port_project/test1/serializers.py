from rest_framework import serializers
from .models import Port, Container

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model= Port
        fields= ('container','no_of_containers','port_no')
        depth=1
class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Container
        fields= '__all__'