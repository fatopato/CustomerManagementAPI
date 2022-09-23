from django.db import models

CUSTOMER_TYPES = (("INDIVIDUAL", "INDIVIDUAL"),
                 ("CORPORATE", "INDIVIDUAL"))


# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    notification_email = models.CharField(max_length=100, default="a@gmail.com")
    customer_type = models.CharField(choices=CUSTOMER_TYPES, default="INDIVIDUAL", max_length=20)

    def __str__(self):
        return self.notification_email



