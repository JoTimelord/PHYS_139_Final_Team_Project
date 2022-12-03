import matplotlib.pyplot as plt
import numpy as np
import random
import math
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
"""
# calculate P on slide 8 on final
# discrete probablity as a function of n0: n0 ~ [0, data.size]
# data, l1, l2 are fixed variables 
def P(n0, data, l1, l2):
    return np.exp(np.log(l1)*np.sum(data[:(n0+1)])-n0*l1+np.log(l2)*np.sum(data[(n0+1):])-(data.size-n0)*l2)

# calculate a_k on slide 9 on final
def a_k(index, data, l1, l2):
    if index == 0:
        return 0
    else:
        sum = 0
        for i in range(index-1):
            sum = P(index, data, l1, l2) + sum
        return sum

# calculate b_k on slide 9 on final
def b_k(index, data, l1, l2):
    sum = 0
    for i in range(index):
        sum = P(index, data, l1, l2) + sum
    return sum
"""
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


# initialize the number of iterations
iterations = 1000
n0_init = 5 # initial value of n0 we decide for when it starts the montecarlo stuff
gamma_init = [8, 1] # initial alpha and beta value of the gamma distribution suggested by Kuti



# Here we processed the data to be 1-d np.array
file = open("processedData.txt", "r")
gravData = file.read().split('\n')
gravData = np.array(list(map(int, gravData)))
#print(n0calc(gravData, 10, 18))

# we then call the montecarlo function
n0, lambda1, lambda2 = montecarlogibbssampling(gravData, iterations, gamma_init, n0_init)

# To-do:
# you guys might wanna re-scale the plot and add captions and title to it
# the main algorithm is done

# plotting n0 
plt.hist(2017+n0, range=(2017, 2200), bins=184)


# plotting l1 and l2
plt.scatter(lambda1, lambda2)

# calculating mean
n0_mean = np.mean(n0)
lambda1_mean = np.mean(lambda1)
lambda2_mean = np.mean(lambda2)
print(lambda1)
print(lambda2)
#print(n0_mean)
#print(lambda1_mean)
#print(lambda2_mean)