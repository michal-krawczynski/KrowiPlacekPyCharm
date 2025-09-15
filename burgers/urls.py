from django.urls import path

from burgers.views import BurgersView, BurgerDetailView

urlpatterns = [
    path('burgers/', BurgersView.as_view(), name='burgers'),
    path('burger/<int:burger_id>/detail/', BurgerDetailView.as_view(), name='burger'),
]