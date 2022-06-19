from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .Serializers import FuncSerializers
from .models import Func

class FuncList(generics.ListAPIView):
    queryset = Func.objects.all()
    serializer_class = FuncSerializers

class FuncDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Func.objects.all()
    serializer_class = FuncSerializers