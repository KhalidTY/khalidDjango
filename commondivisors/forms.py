from django import forms
from .models import TwoNumbers


class TwoNumbersForm(forms.ModelForm):

	number1 = forms.IntegerField(label='Number 1', 
		widget=forms.NumberInput(
			attrs={
			"placeholder": "Enter first number", 
			}))

	number2 = forms.IntegerField(label='Number 2', 
		widget=forms.NumberInput(
			attrs={
			"placeholder": "Enter second number", 
			}))

	class Meta:
		model = TwoNumbers
		fields = [
			"number1",
			"number2",
		]


	def clean_number1(self, *args, **kwargs):
		cleaned_data = super().clean()
		number1_input = cleaned_data.get("number1")

		# Ensure number is non-negative
		# Validation in the model definition enforces numbers greater than 2
		if int(number1_input) < 3:
			raise forms.ValidationError("Invalid Number Entered.")
		return number1_input

	def clean_number2(self, *args, **kwargs):
		cleaned_data = super().clean()

		number2_input = cleaned_data.get("number2")

		# Ensure number is non-negative
		# Validation in the model definition enforces numbers greater than 2
		if int(number2_input) < 3:
			raise forms.ValidationError("Invalid Number Entered.")
		return number2_input

	def clean_lcd_and_gcd(self, *args, **kwargs):
		lcd_and_gcd_input = self.cleaned_data.get("lcd_and_gcd")
		return lcd_and_gcd

	def clean_user(self, *args, **kwargs):
		user_input = self.cleaned_data.get("user")
		return user
	