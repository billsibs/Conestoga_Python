#!/usr/bin/env python3

#Write a program where the user enters two numbers. 
#The program should calculate and display the sum, difference, product and average of the two numbers.

#Collect Some Input. Make sure they're collected as numbers.
number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))

print(f"Your numbers are {number1} and {number2}")

#Do some math
num_sum = number1 + number2
num_dif = number1 - number2
num_pro = number1 * number2
num_avg = (num_sum)/2

#Output the results
print(f"Here are your number calculations:\n " \
f"Summation:  {num_sum}\n " \
f"Difference: {num_dif}\n " \
f"Product:    {num_pro}\n " \
f"Average:    {num_avg}\n  ")