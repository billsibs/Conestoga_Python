#!/usr/bin/env python3

import hrc

filename = 'aerobics.txt'

age = int(input("How old are you? "))

calc = hrc.HeartRateCalculator(age)

max_hrate = ("Your Maximum Heart Rate is " + str(int(calc.max_heart_rate())) + "\n")
min_thrate = ("Your Minimum Target Heart Rate is " + str(int(calc.min_target_heart_rate())) + "\n")
max_thrate = ("Your Maximum Target Heart Rate is " + str(int(calc.max_target_heart_rate())) + "\n")

print(max_hrate + min_thrate + max_thrate)

fw = hrc.FileWriter(filename)
fw.sribble(max_hrate + min_thrate + max_thrate)