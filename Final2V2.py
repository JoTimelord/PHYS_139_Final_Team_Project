import matplotlib.pyplot as plt
import numpy as np

def montecarlogibbssampling(data, niter, gamma_init, lambda_init, n0_init):
    # storing the results for niter of the simulation
    n0vals = np.zeros(niter)
    l1vals = np.zeros(niter)
    l2vals = np.zeros(niter)
    
    # store the updated value for each iterations
    a1, b1 = gamma_init[0], gamma_init[1]
    a2, b2 = gamma_init[0], gamma_init[1]
    l1, l2 = lambda_init[0], lambda_init[1]
    n0 = n0_init

    # simulation process
    for j in range(niter):
        l1, a1, b1 = lambdacalc(data, n0, a1, b1, True) # update l1, a1, b1 values based on previous values
        l2, a2, b2 = lambdacalc(data, n0, a2, b2, False) # update l2, a2, b2 values based on previous values
        n0 = nocalc(data, n0, l1, l2) # update n0 using previous n0 and updated l1, l2 values

        # storing l1, l2, n0 values in np array format for output
        l1vals[j] = l1
        l2vals[j] = l2
        n0vals[j] = n0

    return n0vals, l1vals, l2vals


def nocalc(data, n0, l1, l2):
    # calculates the new value of n0 using the probability function from the slides with the lambda's fixed
    return 0


def lambdacalc(data, n0, a, b, is1):
    # calculates the new lambda value using the probability function from the slides with the other lambda and n0 fixed
    if(is1):
        # use data from 0 to n0
        a1 = a + np.sum(data[:n0])
        b1 = b + n0
        return np.random.gamma(a1, b1), a1, b1
    else:
        # use data from n0 + 1 to N
        a2 = a + np.sum(data[(n0+1):])
        b2 = b + (data.size -  n0)
        return np.random.gamma(a2, b2), a2, b2


# initialize the number of iterations
iterations = 100000
n0_init = 0 # initial value of n0 we decide for when it starts the montecarlo stuff
gamma_init = [8, 1] # initial alpha and beta value of the gamma distribution suggested by Kuti
lambda_init = [0, 0] # initial l1 and l2 values, currently using the dummy values


# Here we processed the data to be 1-d np.array
file = open("processedData.txt", "r")
gravData = file.read().split('\n')
gravData = np.array(list(map(int, gravData)))

# we then call the montecarlo function

n0, lambda1, lambda2 = montecarlogibbssampling(gravData, iterations, gamma_init, lambda_init, n0_init)

# We now have 3 lists of the 3 different values we are trying to find where each index corresponds to a specific
# simulated point. All we have left to do is graph the stuff.

# plotting n0 
plt.hist(2017+n0, density=True, range=(2017, 2200))

# plotting l1 and l2
plt.scatter(lambda1, lambda2)

# calculating mean
n0_mean = np.mean(n0)
lambda1_mean = np.mean(lambda1)
lambda2_mean = np.mean(lambda2)
