#!/usr/bin/env python

from sys import argv
from random import randrange

filename = 'numbers.txt'

if len(argv) > 1:
	x, gen_count = argv
else:
	gen_count = int(input("How many random numbers? "))

num_file = open(filename,'w')
for n in range(0, int(gen_count)):
	num_file.write(str(randrange(1,1000)) + "\n")
num_file.close