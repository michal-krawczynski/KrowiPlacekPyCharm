from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from burgers.models import Burger, BurgersConfig
from burgers.serializers import BurgersModelSerializer, BurgersConfigSerializer


# Create your views here.


class BurgersView(APIView):
    def get(self, request):
        queryset = Burger.objects.all()
        serializer = BurgersModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BurgerDetailView(APIView):
    def get(self, request, burger_id):
        queryset = BurgersConfig.objects.filter(burger_id=burger_id)
        serializer = BurgersConfigSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
