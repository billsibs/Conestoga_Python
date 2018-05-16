#!/usr/bin/env python3

#Create a program that calculates a person’s target heart rate (THR) 
# and maximum heart rate (MHR) for aerobic exercise
# MHR = 220 - age
# Minimum THR = MHR * 50%
# Maximum THR = MHR * 85%

#Define output file
filename = "aerobic.txt"

#Calculate Max heart rate
def max_heart_rate(age):
	mhr = (220 - age)
	return mhr

#Calculate Minimum target heart rate
def min_target_heart_rate(age):
	min_thr = (max_heart_rate(age) * 0.5)
	return min_thr

#Calculate Maximum target heart rate
def max_target_heart_rate(age):
	max_thr = (max_heart_rate(age) * 0.85)
	return max_thr

#Function to write to file.
def write_file(input, file):
    out_file = open(file, 'a')
    out_file.write(input)
    out_file.close()

#Gather Age
age = int(input("How old are you? "))

#Form output strings with results
max_hrate = ("Your Maximum Heart Rate is " + str(int(max_heart_rate(age))) + "\n")
min_thrate = ("Your Minimum Target Heart Rate is " + str(int(min_target_heart_rate(age))) + "\n")
max_thrate = ("Your Maximum Target Heart Rate is " + str(int(max_target_heart_rate(age))) + "\n")

#Print results to screen
print(max_hrate + min_thrate + max_thrate)

#Print results to file
write_file(max_hrate, filename)
write_file(min_thrate, filename)
write_file(max_thrate, filename)

#Notify user where results can be found on disk
print(f"Results written to {filename}")
