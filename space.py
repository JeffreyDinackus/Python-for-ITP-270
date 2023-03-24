#!/bin/python

weight = int(input("enter your weight on earth: "))

planet = int(input("Enter the code for the planet you are on: "))

if planet == 1:
	conv = float(.91 * weight)
	print("Your weight is " + str(conv))

elif planet == 2:
	conv = float(.38 * weight)
	print("Your weight is " + str(conv))

elif planet == 3:
	conv = float(2.34 * weight)
	print("Your weight is " + str(conv))

elif planet == 4:
	conv = float(1.06 * weight)
	print("Your weight is " + str(conv))

elif planet == 5:
	conv = float(.92 * weight)
	print("Your weight is " + str(conv))

elif planet == 6:
	conv = float(1.19 * weight)
	print("Your weight is " + str(conv))