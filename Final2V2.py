import matplotlib.pyplot as plt
import numpy as np
import random
import math
from matplotlib.animation import FuncAnimation
import scipy.stats

def montecarlogibbssampling(data, niter, gamma_init, n0_init):
    # storing the results for niter of the simulation
    n0vals = np.zeros(niter)
    l1vals = np.zeros(niter)
    l2vals = np.zeros(niter)
    
    # store the updated value for each iterations
    a1, b1 = gamma_init[0], gamma_init[1]
    a2, b2 = gamma_init[0], gamma_init[1]
    l1, l2 = 0, 0
    n0 = n0_init

    # simulation process
    for j in range(niter):
        l1, a1, b1 = lambdacalc(data, n0, a1, b1, True) # update l1, a1, b1 values based on previous values
        l2, a2, b2 = lambdacalc(data, n0, a2, b2, False) # update l2, a2, b2 values based on previous values
        #print("l1, a1, b1", l1, a1, b1)
        #print("l2, a2, b2: ", l2, a2, b2)
        n0 = n0calc(data, l1, l2) # update n0 using updated l1, l2 values
        #print("n0: ", n0)

        # storing l1, l2, n0 values in np array format for output
        l1vals[j] = l1
        l2vals[j] = l2
        n0vals[j] = n0

    return n0vals, l1vals, l2vals

def n0calc(data, l1, l2):
    # calculates the new value of n0 using the probability function from the slides with the lambda's fixed
    N = data.size
    n0list = np.linspace(start=0, stop=N-1, num=N)
    n0prob = np.zeros(N)
    sum = 0
    for i in data:
        element = math.factorial(i)
        element = float(element)
        sum = sum + np.log(element)
    for i in range(N):
        n0 = n0list[i]
        sum1 = np.sum(data[0:i+1])
        sum2 = np.sum(data[i+1:])
        exponent = np.log(l1) * sum1 - n0 * l1 + np.log(l2)*sum2  - (N-n0) * l2 - sum
        #print("exponent: ", exponent)
        u = np.exp(exponent)
        n0prob[i] = u
    return int(random.choices(n0list, weights=n0prob)[0])


def lambdacalc(data, n0, a, b, is1):
    # calculates the new lambda value using the probability function from the slides with the other lambda and n0 fixed
    if(is1):
        # use data from 0 to n0
        a1 = a + np.sum(data[:(n0+1)])
        b1 = b + n0
        #return np.random.gamma(a1, b1), a1, b1
        return np.random.gamma(a1,1/b1), a1, b1
    else:
        # use data from n0 + 1 to N
        a2 = a + np.sum(data[(n0+1):])
        b2 = b + (data.size -  n0)
        return np.random.gamma(a2,1/b2), a2, b2

def surfaceplot(n0, l1, l2):
    distance = np.sqrt(np.square(n0-np.mean(n0))+np.square(l1-np.mean(l1))+np.square(l2-np.mean(l2)))
    sigma = np.std(distance)
    filterarr = distance <= sigma
    filterarr2 = distance > sigma
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(n0[filterarr], l1[filterarr], l2[filterarr], color='blue', label=r'inside 1$\sigma$')
    ax.scatter(n0[filterarr2], l1[filterarr2], l2[filterarr2], color='red', label=r'outside 1$\sigma$')
    ax.scatter(np.mean(n0), np.mean(l1), np.mean(l2), color='black', label='mean')
    ax.set_xlabel(r'$n_0$')
    ax.set_ylabel(r'$\lambda_1$')
    ax.set_zlabel(r'$\lambda_2$')
    ax.legend()
    ax.set_title("One Sigma region")
    plt.savefig('interval.png')

# initialize the number of iterations
iterations = 10000
n0_init = 5 # initial value of n0 we decide for when it starts the montecarlo stuff
gamma_init = [8, 1] # initial alpha and beta value of the gamma distribution suggested by Kuti



# Here we processed the data to be 1-d np.array
file = open("processedData.txt", "r")
gravData = file.read().split('\n')
gravData = np.array(list(map(int, gravData)))
#file = open("GravitationalWaveDetectionRecord_teamA.txt", "r")
#print(n0calc(gravData, 10, 18))

# iterate from i = 2017 to i = 2200
values = range(184)
with open('years.txt', 'w') as f:
    for i in values:
        #print(2017+i)
        f.write(str(2017+i))
        if 2017+i == 2200:
            break
        f.write('\n')
yearsfile = open("years.txt", "r")
years = yearsfile.read().split('\n')
years = np.array(list(map(int, years)))
plt.scatter(years, gravData, s=30, facecolors='none', edgecolors='b', marker = "o")
plt.title('Gravitational Wave Detection Record')
plt.xlabel('Year')
plt.ylabel('recorded gravitational wave events')
#plt.show()
plt.savefig("problem0.png")

# we then call the montecarlo function
n0, lambda1, lambda2 = montecarlogibbssampling(gravData, iterations, gamma_init, n0_init)

# To-do:
# you guys might wanna re-scale the plot and add captions and title to it
# the main algorithm is done

# plotting n0 
plt.hist(2017+n0, range=(2017, 2200), density = True, bins=184, edgecolor='dimgrey', linewidth=1.2, color='indianred')
plt.xlim([2060, 2180])
plt.ylim([0, 0.25])
plt.title('$n_0$ probability distribution')
plt.xlabel('n')
plt.ylabel('P($n_0|x_{1:N}$)',rotation=0)
#plt.show()
plt.savefig("problemc1.png")

surfaceplot(n0, lambda1, lambda2)

# plotting l1 and l2
plt.scatter(lambda1, lambda2, s=2, c='indianred', marker=".")
plt.xlim([10.4, 10.6])
plt.ylim([17.8, 18.4])
plt.title('$\lambda_1$, $\lambda_2$ from Gibbs sampling')
plt.xlabel('$\lambda_1$')
plt.ylabel('$\lambda_2$',rotation=0)
#plt.show()
plt.savefig("problemc2.png")
#plt.close()

# calculating mean
n0_mean = np.mean(n0)
lambda1_mean = np.mean(lambda1)
lambda2_mean = np.mean(lambda2)
