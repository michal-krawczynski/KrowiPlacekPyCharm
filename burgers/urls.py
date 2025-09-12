from django.urls import path

from burgers.views import BurgersView

urlpatterns = [
    path('burgers/', BurgersView.as_view(), name='burgers'),
]