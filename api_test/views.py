from django.shortcuts import render
from rest_framework import viewsets
from .models import MachineL
from .serializers import MachineSerializer
class MachineView(viewsets.ModelViewSet):
    queryset=MachineL.objects.all()
    serializer_class=MachineSerializer

