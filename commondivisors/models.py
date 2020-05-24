from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

# Create your models here.
class TwoNumbers(models.Model):

	number1	= models.PositiveIntegerField(blank=False)
	number2	= models.PositiveIntegerField(blank=False)

	# number1	= models.PositiveIntegerField(blank=False, validators=[MinValueValidator(3)])
	# number2	= models.PositiveIntegerField(blank=False, validators=[MinValueValidator(3)])
