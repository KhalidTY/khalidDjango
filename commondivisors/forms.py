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
		number1_input = self.cleaned_data.get("number1")

		# Ensure number is greater than 2
		if int(number1_input) < 3:
			raise forms.ValidationError("Invalid Number Entered.")
		return number1_input

	def clean_number2(self, *args, **kwargs):
		number2_input = self.cleaned_data.get("number2")

		# Ensure number is greater than 2
		if int(number2_input) < 3:
			raise forms.ValidationError("Invalid Number Entered.")
		return number2_input
