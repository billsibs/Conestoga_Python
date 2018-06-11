#!/usr/bin/env python

input_file = 'numbers.txt'
output_file = 'sum.txt'
sum_nums = 0

num_file = open(input_file)

for number in num_file:
	temp = int(number) % 2
	if temp == 0:
		print(number)
		sum_nums = sum_nums + int(number)

num_file.close()
out_file = open(output_file, 'w')

message = f'The sum of the even numbers in {input_file} is: {sum_nums}\n'
#print(message)
out_file.write(message)

out_file.close()