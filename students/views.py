from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework import filters

# Create your views here.

class StudentViewset(viewsets.ModelViewSet):
    serializer_class= StudentSerializer 
    queryset = Student.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields=['num_ordre','name','genre','nni','bac_id','formation','level']