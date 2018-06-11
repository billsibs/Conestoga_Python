#!/usr/bin/env python

#Prompt the user for a number (x) and then generate x random numbers. 
#The random numbers should be in the range of 1 to 1000
#Output the list of the numbers to a text file called numbers.txt

#Import modules. Added argv for fun so script can be run without prompting
from sys import argv
from random import randrange

#Variable declaration
filename = 'numbers.txt'

#Logic to see if user provided value at execution, if not then prompt for input
if len(argv) > 1:
	x, gen_count = argv
else:
	gen_count = int(input("How many random numbers? "))

#Open file, generate random numbers, write to file, and finally close
num_file = open(filename,'w')
for n in range(0, int(gen_count)):
	num_file.write(str(randrange(1,1000)) + "\n")
num_file.close