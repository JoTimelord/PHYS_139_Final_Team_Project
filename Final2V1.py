import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10)
rv = np.random.gamma(4, 1, 10000)
print(rv)
plt.hist(rv, bins=50, density=True)
plt.show()

a = 1
b=1

<<<<<<< HEAD
def montecarlogibbssampling(data, niter, gamma_init, lambda_init, n0_init):
=======
def montecarlogibbssampling(data, niter, a_init, b_init, n0_init):
>>>>>>> f4739bb873aee73a10fdd3c5452d09c5cb95d75f
    # storing the results for niter of the simulation
    n0vals = np.zeros(niter)
    l1vals = np.zeros(niter)
    l2vals = np.zeros(niter)
    
    # store the updated value for each iterations
<<<<<<< HEAD
    a1, b1 = gamma_init[0], gamma_init[1]
    a2, b2 = gamma_init[0], gamma_init[1]
    l1, l2 = lambda_init[0], lambda_init[1]
=======
    a1, b1 = a_init, b_init
    a2, b2 = a_init, b_init
    l1, l2 = 0, 0
>>>>>>> f4739bb873aee73a10fdd3c5452d09c5cb95d75f
    n0 = n0_init

    for j in range(niter):
        l1, a1, b1 = lambdacalc(data, n0, a1, b1, True)
        l2, a2, b2 = lambdacalc(data, n0, a2, b2, False)
        n0 = nocalc(data, n0, l1, l2)

        l1vals[j] = l1
        l2vals[j] = l2
        n0vals[j] = n0

<<<<<<< HEAD
    return n0vals, l1vals, l2vals
=======
    return n0, l1vals, l2vals
>>>>>>> f4739bb873aee73a10fdd3c5452d09c5cb95d75f


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
Iterations = 100000
<<<<<<< HEAD
n0_init = 0 # initial value of n0 we decide for when it starts the montecarlo stuff
gamma_init = [8, 1] # initial alpha and beta value of the gamma distribution suggested by Kuti
lambda_init = [0, 0] # initial l1 and l2 values, currently using the dummy values
=======
noFirst = 0 # initial value of n0 we decide for when it starts the montecarlo stuff
a, b = 8, 1 # initial alpha and beta value suggested by Kuti
>>>>>>> f4739bb873aee73a10fdd3c5452d09c5cb95d75f

# Here we take in the data
gravData = 0 # replace zero with whatever data we get

# we then call the montecarlo function

<<<<<<< HEAD
n0, lambda1, lambda2 = montecarlogibbssampling(gravData, Iterations, gamma_init, lambda_init, n0_init)
=======
n0, lambda1, lambda2 = montecarlogibbssampling(gravData, noFirst, Iterations, a, b)
>>>>>>> f4739bb873aee73a10fdd3c5452d09c5cb95d75f
print("n0", n0)
print("lambda1", lambda1)
print("lambda2", lambda2)

# We now have 3 lists of the 3 different values we are trying to find where each index corresponds to a specific
# simulated point. All we have left to do is graph the stuff.
