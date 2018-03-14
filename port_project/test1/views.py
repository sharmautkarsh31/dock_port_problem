from django.shortcuts import render
from rest_framework import viewsets
from .models import Port, Container
from .serializers import PortSerializer, ContainerSerializer
from rest_framework.response import Response
from django.db.models import Sum

# Create your views here.
class PortViewset(viewsets.ModelViewSet):
    queryset = Port.objects.all()
    serializer_class = PortSerializer


class ContainerPositionViewset(viewsets.ViewSet):
    queryset = Container.objects.all()
    def list(self, request):
        sum_container= Port.objects.aggregate(sum=Sum('no_of_containers'))
        sum_c=sum_container['sum']
        port_set= list(Port.objects.all())[::-1]
        container_counter=0
        port_index=0
        for i in range(5):
            for j in range(5):
                for k in range(10):
                    pos=str(i)+','+str(j)+','+str(k)
                    if container_counter<port_set[port_index].no_of_containers:
                        port_id=port_set[port_index]
                        container_counter=container_counter+1
                        print(container_counter,'----------')
                    else:
                        print(container_counter,'^^^^^^^^^^')
                        container_counter=1
                        port_index=port_index+1
                        port_id = port_set[port_index]
                    Container.objects.create(
                        position= pos,
                        port=port_id
                    )
                    sum_c= sum_c-1
                    if sum_c==0:
                        queryset = Container.objects.all()
                        serializer = ContainerSerializer(queryset, many=True)
                        return Response(serializer.data)
                    
                    #test
