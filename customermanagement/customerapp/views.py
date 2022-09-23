# Create your views here.
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from .models import Customer
from .serializers import CustomerSerializer


class CustomerRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerListCreateAPIView(ListCreateAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer