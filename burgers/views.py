from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from burgers.models import Burger
from burgers.serializers import BurgersModelSerializer


# Create your views here.


class BurgersView(APIView):
    def get(self, request):
        queryset = Burger.objects.all()
        serializer = BurgersModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)