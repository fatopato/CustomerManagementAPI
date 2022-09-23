from rest_framework import serializers
from .models import Customer
import re
from .api_exceptions import CustomerNotFoundException, InvalidCustomerRequestException

EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class CustomerSerializer(serializers.ModelSerializer):

    def validate_notification_email(self, value):
        if not re.fullmatch(EMAIL_REGEX, value):
            raise InvalidCustomerRequestException("Notification email is not valid")
        else:
            return value

    def validate_id(self, value):
        if value != None:
            raise InvalidCustomerRequestException("Customer ID must be null while saving")

    def validate(self, data):

        if Customer.objects.filter(notification_email=data['notification_email'],
                                     customer_type=data['customer_type']).exists():
            raise InvalidCustomerRequestException("Notification email has already used with the customer type")

        else:
            return data

    class Meta:
        model = Customer
        fields = ["id", "notification_email", "customer_type"]




