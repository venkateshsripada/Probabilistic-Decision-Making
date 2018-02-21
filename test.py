import matplotlib.pyplot as plt
import numpy as np

'''

#initialize distribution

dist = np.full((100, 100), 1/(100*100))

#initialize robot in the world.. TODO randomly
world = np.zeros((100,100))
robot1 = world[0][0]
robot2 = world[80][0]


def move_up():
	robot[i][j] = robot[i+1][j]
for i in range(world[0:][0]):
	for j in range(world[0][0:]):
		robot1 = robot1 + world[i][j]
		robot2 = robot2 + world[i][j]
#place the target and surrogates. Function written because we are manually placing the targets now
def target_position(a,b):
	target = world[a][b]
	surr_target1 = world[a-20][b-20]
	surr_target2 = world[a+20][b+20]
	return target, surr_target1, surr_target2
#define target so that it can be iterated over in the pdf
def target():
	probability around target  is high > 1/100*100

#probability density function of target
def pdf(t):
	dist = np.full((100, 100), 1/(100*100))
	dist = g
	#print norm.cdf(x, mean, std)

#define move i.e wherever there is maximum kld
scipy.stats.entropy(dist)

#Update probabilities
print target(50,50)

'''


# def getangle(p1, p2):  # angle between start and last point of the line
# 	x1, y1 = p1
# 	x2, y2 = p2
# 	dX = x2 - x1
# 	dY = y2 - y1
# 	global rads
# 	rads = math.atan2(-dY, dX)
# 	print "angle:", math.degrees(rads)
# 	return math.degrees(rads)

''' ROBOT MOTION 

# Robot_motion UP --taking only indexes as i and j and not value world[i][j]
def move_up(i, j):
	for p in range(len(world)):  # x axis
		for q in range(len(world)):  # y axis
			i, j = i, j - 1


def move_right(i, j):
	for p in range(0, 100):
		# for j in range(len(world)-1):
		i, j = i + 1, j
		print i, j
		if (i == 100) or (j == 100):
			move_down(i, j)
			print i, j
		plt.plot(i, j, 'ro')
		plt.show()


def move_left(i, j):
	for p in range(len(world)):
		# for q in range(len(world)):
		i, j = i - 1, j


def move_down(i, j):
	# for p in range(len(world)):
	for q in range(len(world)):
		i, j = i, j + 1
		if (i % 2 != 0):
			move_left(i, j)
'''