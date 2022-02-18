from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
# Create your views here.

from .models import Tanks
from .serializers import TankSerializer

class TanksViewSet(viewsets.ViewSet):
    def list(self, request): 
        tanks = Tanks.objects.all()
        serializer = TankSerializer(tanks, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TankSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrive(self, request, pk=None):
        tank = Tanks.objects.get(id=pk)
        serializer = TankSerializer(tank)
        return Response(serializer.data)
    

    def update(self, request, pk=None):
        tank = Tanks.objects.get(id=pk)
        serializer = TankSerializer(instance=tank, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        tank = Tanks.objects.get(id=pk)
        tank.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
