from django.shortcuts import render
from .models import TwoNumbers
from .forms import TwoNumbersForm
from django.http import Http404


# Function to find a list of divisors of a number
def divisors_list(num):
    divisors = []
    if num % 2 == 0:
        divisors.append(2)
        divisors.append(num // 2)
        upper_search_limit = num // 4
        i = 3
        while i <= upper_search_limit + 1:
            if num % i == 0:
                divisors.append(i)
                divisors.append(num // i)
                upper_search_limit = upper_search_limit // 2
            i += 1
    else:
        upper_search_limit = num // 4
        i = 3
        while i <= upper_search_limit + 1:
            if num % i == 0:
                divisors.append(i)
                divisors.append(num // i)
                upper_search_limit = upper_search_limit // 2
            i += 2
    divisors = list(set(divisors))
    divisors.sort()
    return divisors


# Function to solve the given problem
def solve(nums):
	msg = []
	num1_divisors_list = divisors_list(nums[0])
	num2_divisors_list = divisors_list(nums[1])
	common_divisors_list = list(set(num1_divisors_list) & set(num2_divisors_list))
	common_divisors_list.sort()

	msg.append("Number 1: " + str(nums[0]))
	msg.append("Number 2: " + str(nums[1]))
	msg.append("Divisor list of first number: " + str(num1_divisors_list))
	msg.append("Divisor list of second number: " + str(num2_divisors_list))

	if len(num1_divisors_list) == 0 or len(num2_divisors_list) == 0:
	    msg.append("Common divisor is out of question as at least one of the numbers is a prime.")
	elif len(common_divisors_list) == 0:
	    msg.append("The two numbers don't even have a single common divisor.")
	elif len(common_divisors_list) == 1:
	    msg.append("The two numbers have only one common divisor: " + str(common_divisors_list))
	else:
	    msg.append("Common divisors list: " + str(common_divisors_list))
	    msg.append("Therefore, the two numbers' smallest and greatest common divisors are " + str(common_divisors_list[0]) + " and " + str(common_divisors_list[-1]) + ", respectively.")

	return msg


# Create your views here.
def twonumbers_view(request, *args, **kwargs):
	numbers_form = TwoNumbersForm(request.POST or None)
	
	# good_request = None
	
	if numbers_form.is_valid():

		good_request = request

		valid_two_numbers = []
		valid_two_numbers.append(int(numbers_form.cleaned_data['number1']))
		valid_two_numbers.append(int(numbers_form.cleaned_data['number2']))
		
		# numbers_form = TwoNumbersForm()

		solution = solve(valid_two_numbers)
		
		context = {
			"result": solution
		}
		
		return render(request, "commondivisors/solution.html", context)
		
		# numbers_form = TwoNumbersForm()

	# if good_request != None:
	# 	request = good_request
	# 	numbers_form = TwoNumbersForm(request.POST)

	context = {
		"form": numbers_form,
	}
	
	return render(request, "commondivisors/twonumbers.html", context)

