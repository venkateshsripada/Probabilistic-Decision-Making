#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.animation
import matplotlib.axes
from scipy.stats import norm
from scipy.stats import rv_discrete
from scipy.stats import entropy
import pdb
import math

# Initialize world. We want to have the environment
# World from human perspective

world = np.full((100, 100), float(3))  # initial empty matrix
world[4][1] = 5
sensed = []								#All the sensor measurements
path = [(0,0)]

'''Range Sensor: OUTPUT set of all measurements obtained at the instant'''

def range_s(i, j, len_beam=3):
	sensed_measure = []

	#getangle(sensed[0], sensed[-1])  # gives us angle between start and end grids in range of beam
	k_beams(7)                        # 7 beams are generated
	#plt.plot(i,j,'g2')
	print "Position of robot:", i,j
	plt.plot(i,j,'ro')
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
	global sensed

	sensed.extend(sensed_measure)
	pmf()
	print "sensed:", sensed

	
	
	ax = plt.gca()
	ax.set_xlim(0,30)
	ax.set_ylim(-1,10)

#	for i,j in sensed:

#		plt.plot(i,j,'ro')
	#plt.autoscale()
	plt.show()

	sensed = []


def line(p1, p2):				#Function to obtain points between start and end

	x0, y0 = p1
	x1, y1 = p2
	deltax= x1 - x0
	deltay= y1 - y0
	deltaerr= abs(deltay / deltax)
	error= 0.0  #No error at start
	y = y0
	for x in range(x0, x1):
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
	#print "middle points", sensed



def k_beams(number_beams=7):  # number of beams that should pass between 0 and 80 degrees
	beams = np.linspace(0, 80, number_beams)
	beams = map(int, beams)
	global all_beam_angle
	all_beam_angle = []
	for k in beams:
		all_beam_angle.append(k)

	print "All beams:", all_beam_angle



'''Define the probability density function in z so that each measurement has a value'''
def pmf():
	measurement_value = []
	KL_Divergence = []
	K_prev = 0
	for i in range(len(sensed)):
		row, col = sensed[i]
		measurement = world[row][col] 	#values are given to the indices in list named sensed
		#print "measurement", measurement				#measurement gives the value of the belief of target in each grid


		mu = measurement
		variance = 1
		sigma = math.sqrt(variance)		#generating a normal distribution
		x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
		# This is the first measurement to be compared with everything else
		norm_x = norm.pdf(x)
		measurement_value.append(norm_x)		#measuement_value is a list of arrays

		try:							#we get changed measurement values in the next cells
			row1, col1 = sensed[i +1]
			measurement1 = world[row1][col1]
			measurement1 = measurement1 + (measurement/ (len(sensed)-1))
			#print "measurement1", measurement1

			mu = measurement1
			variance = 1
			sigma = math.sqrt(variance)		#generating a normal distribution
			x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
			#  Adding all of the normalized distribtuions to measurement_value. This will form the first layer of the tree
			norm_x = norm.pdf(x)
			measurement_value.append(norm_x)		#measuement_value is a list of arrays


		except:
			pass

		if i >=1:
			KLD = entropy(measurement_value[i-1], measurement_value[i])
			print "KLD at:",i,"=", KLD
			if KLD > 2 * K_prev:
				print "Increase in KLD at:", sensed[i]
				path.append(sensed[i])			#move the robot in the direction of maximum KLD
				print "\npath is:", path
			KL_Divergence.append(KLD)

			K_prev = KLD
			print "\nK_prev:",i,"=", K_prev

		'''bel(i, j) = bel(i+1,j)/n
		range.append(bel(i,j))
		'''





	#print "meassurement value:", measurement_value
		# Mean will be at 0 because the initial distribution is very less (1/100*100)
		#plt.plot(x, mlab.normpdf(x, mu, sigma))
		#plt.show()


#TODO 2
def prob():
	prob_xz = (prob_zx * prob_x)/ prob_z
	prob_x = prob_xz




if __name__ == '__main__':

	
	# j = 0
	# for i in range(len(world)):
	 	#for j in range(len(world)):
	# 	i,j = i+1, j
			# if i%100 == 0:
			# 	i,j = i,j -1
			# elif i%2 != 0:
			# 	i,j = i-1,j
			# elif i == 0:
			# 	i,j = i,j+1
			# else:
			# 	i,j = i+1,j
			# #plt.plot(i, j, 'go')
			# #plt.show()
			# print i,j
	#	range_s(i, j)
	
	for row in path:
		i,j = row
		range_s(i,j)

		print "\n\ni,j:", i,j

		# 	ani = matplotlib.animation.FuncAnimation(fig, range_s(i, j), frames=100, repeat=False)
		# plt.show()
	# plt.plot(sensed, 'ro')
	# axes = plt.gca()
	# axes.set_ylim([-5.0, 20.0])
	# axes.set_xlim([-5.0, 5.0])
	# plt.show()

'''
	x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)

	print norm.ppf(0.3)
	plt.plot(x, norm.pdf(x))
	plt.show()
'''
