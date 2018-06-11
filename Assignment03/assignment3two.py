#!/usr/bin/env python

#Read in the file (numbers.txt) from previous script
#Sum only the even numbers
#Output the sum of the even numbers to a new file called num.txt

#Declare variables.
input_file = 'numbers.txt'
output_file = 'sum.txt'
sum_nums = 0

#Open input file
num_file = open(input_file)

#Use modulus to check if odd or even then add the values into a single variable
for number in num_file:
	temp = int(number) % 2
	if temp == 0:
		#print(number) #Debug line
		sum_nums = sum_nums + int(number)

#Close input file
num_file.close()

#Open output file
out_file = open(output_file, 'w')

#Print message and then write to output file
message = f'The sum of the even numbers in {input_file} is: {sum_nums}\n'
print(message)
print(f"Answer written to {output_file}\n")
out_file.write(message)

#Close output file
out_file.close()