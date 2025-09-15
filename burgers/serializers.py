from rest_framework import serializers

from burgers.models import Burger, BurgersConfig


class BurgersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burger
        fields = '__all__'


class BurgersConfigSerializer(serializers.ModelSerializer):
    ingredients = serializers.SerializerMethodField()
    class Meta:
        model = BurgersConfig
        fields = ('burger', 'ingredients',)

    def get_ingredients(self, obj):
        ingredients = obj.ingredients.all()
        ingredients_names = []
        for ingredient in ingredients:
            ingredients_names.append(ingredient.name)
        return ingredients_names