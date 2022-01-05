from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CrackerSerializers
from .models import Cracker
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class StudentCurd(generics.ListCreateAPIView):
    queryset = Cracker.objects.all()
    serializer_class = CrackerSerializers
    permission_classes = [permissions.AllowAny]


class StudentCurdd(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cracker.objects.all()
    serializer_class = CrackerSerializers
    permission_classes = [permissions.AllowAny]