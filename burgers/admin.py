from django.contrib import admin

from burgers.models import Burger, BurgersConfig, Product


# Register your models here.
@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)

@admin.register(BurgersConfig)
class BurgersConfigAdmin(admin.ModelAdmin):
    list_display = ("burger", 'get_ingredients',)

    def get_ingredients(self, obj):
        return ", ".join([ingredient.name for ingredient in obj.ingredients.all()])

    get_ingredients.short_description = 'Ingredients'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)