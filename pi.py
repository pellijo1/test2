#!/usr/bin/python3
"""
Simplistic PI calculation

Simple PI calculation using Monte Carlo.
"""

import math, random

total  = 0
inside = 0
while True :
	for i in range(100000) :
		x, y = random.random(), random.random()
		total += 1
		if not math.sqrt(x*x+y*y)>1 :
			inside += 1
	print("Total={0}, inside={1}, pi={2}".format(total, inside, 4.0*float(inside)/float(total)))
