import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#initialize distribution

distr = np.full((100, 100), 1/(100*100))
print len(distr[0:])

def motion_sides():
	position = [][]
	for i in range(len(distr[0:])):
		if i % 2 == 0:  # Moving right
			for j in range(len(distr[:0])):
				position = (distr[i+1][j + 1])
				# Finding target and informing
				if position[i][j] == distr[30][30]:
					print "Information Found"
					return i, j
				#Finding sub target and taking another action
				elif position[i][j] == distr[50][60]:
					print "Taking another route"
		else:   # Moving left
			for j in range(len(distr[0:])):
				position = (distr[i+1][j-1])
				if position[i][j] == distr[30][30]:
					print "New Information found"
					return i,j
			#plt.plot(position, 'ro')
			#plt.show()

# Belief update step/ function
def update():
	#belief of x is prob(x|target)*bel(x-1). So, prob(x|target) is generated using bayes rule
	prob_x_t = prob_t_x * prob_x / prob_t

	belief_x = prob[][]
	prob[i+1][j] = prob[i+1][j] + prob_old / (100*100 - 1)


'''
#initialize robot in the world.. TODO randomly
world = np.zeros((100,100))
robot1 = world[0][0]
robot2 = world[80][0]

for i in range(world[0:][0]):
	for j in range(world[0][0:])
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
if __name__ == '__main__':
	motion()