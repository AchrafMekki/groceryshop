from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(AbstractUser):
   TITLE_CHOICES = {
      "Mr": "Mr",
      "Mrs": "Mrs",
      "Miss": "Miss",
      "Dr": "Dr",
   }
   username = models.CharField(max_length=50, unique=True)
   date_of_birth = models.DateField(null=True, blank=True)
   title = models.CharField(max_length=50, choices=TITLE_CHOICES, null=True, blank=True)

   class Meta:
       constraints = [
          models.CheckConstraint(
              name='%(app_label)s_%(class)s_title_check',
             check=models.Q(title__in=['Mr', 'Mrs', 'Miss', 'Dr']),
          )
       ]