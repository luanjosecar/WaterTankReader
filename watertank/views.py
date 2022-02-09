from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

class TanksViewSet(viewsets.ViewSet):
    def list(self, request):
        pass
    def create(self, request):
        pass
    def retrive(self, request, pk=None):
        pass