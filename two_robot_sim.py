import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#initialize distribution

dist = np.full((100, 100), 1/(100*100))

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

