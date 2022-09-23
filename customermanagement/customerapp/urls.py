from django.contrib import admin
from django.urls import path, include
from .views import CustomerListCreateAPIView, CustomerRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('', CustomerListCreateAPIView.as_view()),
    path('<int:pk>/', CustomerRetrieveUpdateDeleteAPIView.as_view()),

]