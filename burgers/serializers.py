from rest_framework import serializers

from burgers.models import Burger


class BurgersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burger
        fields = '__all__'