from django.shortcuts import render
from djangoapi.quickstart.models import Companies
from rest_framework import viewsets, permissions
from djangoapi.quickstart.serializers import CompaniesSerializer


# Create your views here.

class CompaniesViews(viewsets.ModelViewSet):
    """
    API endpoint that allows user to see all the financial data of the companies
    """
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    permission_classes = [permissions.IsAuthenticated]
