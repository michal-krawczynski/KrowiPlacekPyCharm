from django.db import models

# Create your models here.
class Burger(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BurgersConfig(models.Model):
    burger = models.OneToOneField(Burger, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Product)
    def __str__(self):
        return self.burger.name