#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import rv_discrete
import pdb
import math

# Initialize world. We want to have the environment
# World from human perspective

world = np.full((100, 100), 1/(100*100))  # initial empty matrix
sensed = []								#All the sensor measurements

# Range Sensor: OUTPUT set of all measurements obtained at the instant
# TODO probabilities
def range_s(i, j, len_beam=3):
	sensed_measure = []

	#getangle(sensed[0], sensed[-1])  # gives us angle between start and end grids in range of beam
	k_beams(7)                        # 7 beams are generated

	for t in all_beam_angle:
		x_1 = i + len_beam*(np.cos(np.deg2rad(t)))
		y_1 = j + len_beam*(np.sin(np.deg2rad(t)))
		p = int(round(x_1)), int(round(y_1))
		if p in sensed_measure:			#To ensure two measurements from same grid are not obtained
			pass
		else:
			sensed_measure.append(p)
	for val in sensed_measure:
		#print "val", val
		line((i,j), (val))					#gives grids that are in between start (i,j) and end points (val)

	print "Measurement from sensors",sensed_measure
	sensed.extend(sensed_measure)



def line(p1, p2):				#Function to obtain points between start and end

	x0, y0 = p1
	x1, y1 = p2
	deltax= x1 - x0
	deltay= y1 - y0
	deltaerr= abs(deltay / deltax)
	error= 0.0  #No error at start
	y = y0
	for x in range(x0, x1):
		#plt.plot(x,y,'ro')
		#plt.show()
		#print x, y
		points = x,y
		if points in sensed:
			pass
		else:
			sensed.append(points)

		error = error + deltaerr
		while error >= 0.5:
			y = y + np.sign(deltay) * 1
			error= error - 1.0
				#plotting
			#p = (x,y)
			#p = tuple(p)
			#sensed.append(p)
			#print "sensed", sensed
			# plt.plot(sensed)
			# axes = plt.gca()
			# axes.set_ylim([-5.0, 20.0])
			# axes.set_xlim([-5.0, 5.0])
			# plt.show()
	print "middle points", sensed

'''Not used
def lines(i, j, len_beam=3):
	for t in all_beam_angle:
		for x in range(i, i + len_beam):
			for y in range(j, j + len_beam):
				if y == math.tan(t) * (x - i) + j:
					print "Angle:", t
					print x, y
'''

def k_beams(number_beams=7):  # number of beams that should pass between 0 and 60 degrees
	beams = np.linspace(0, 80, number_beams)
	beams = map(int, beams)
	global all_beam_angle
	all_beam_angle = []
	for k in beams:
		all_beam_angle.append(k)

	print "All beams:", all_beam_angle



#TODO 1 define the probability density function in z so that each measurement has a value
def pmf():
	for i in range(len(sensed)):
		row, col = sensed[i]
		measurement = world[row][col] 	#values are given to the indices in list named sensed

	sigma = 



#TODO 2
def prob():
	prob_xz = (prob_zx * prob_x)/ prob_z
	prob_x = prob_xz




if __name__ == '__main__':
	range_s(2, 2)
	print "sense",sensed
	# plt.plot(sensed, 'ro')
	# axes = plt.gca()
	# axes.set_ylim([-5.0, 20.0])
	# axes.set_xlim([-5.0, 5.0])
	# plt.show()
	pmf()
'''
	x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)

	print norm.ppf(0.3)
	plt.plot(x, norm.pdf(x))
	plt.show()
'''