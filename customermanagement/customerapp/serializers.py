from rest_framework import serializers
from .models import Customer
import re
from .api_exceptions import NotificationEmailAlreadyExistsException, InvalidCustomerRequestException

EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class CustomerSerializer(serializers.ModelSerializer):

    def validate(self, data):

        # id validation
        if "id" in data.keys():
            raise InvalidCustomerRequestException("Customer ID must be null while saving")

        # notification_email validation
        if not re.fullmatch(EMAIL_REGEX, data["notification_email"]):
            raise InvalidCustomerRequestException("Notification email is not valid")

        # notification_email uniqueness validation
        if Customer.objects.filter(notification_email=data['notification_email'],
                                     customer_type=data['customer_type']).exists():
            raise NotificationEmailAlreadyExistsException()

        else:
            return data

    class Meta:
        model = Customer
        fields = ["id", "notification_email", "customer_type"]
        extra_kwargs = {'id': {'read_only': False, 'required': False}}




