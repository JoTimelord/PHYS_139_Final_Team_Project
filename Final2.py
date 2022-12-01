import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma


def montecarlogibbssampling(data, noinit, niter, npoints):
    novals = [0 for i in range(npoints)]
    l1vals = [0 for i in range(npoints)]
    l2vals = [0 for i in range(npoints)]
    for i in range(npoints):
        notemp = noinit
        l1temp = 0
        l2temp = 0

        for j in range(niter):
            l1temp = lambdacalc(data, noinit, l1temp, True)
            l2temp = lambdacalc(data, noinit, l2temp, False)
            notemp = nocalc(data, notemp, l1temp, l2temp)

        novals[i] = notemp
        l1vals[i] = l1temp
        l2vals[i] = l2temp

        return novals, l1vals, l2vals


def nocalc(data, noval, l1, l2):
    # calculates the new value of n0 using the probability function from the slides with the lambda's fixed
    return 0


def lambdacalc(data, noinit, lam, is1):
    # calculates the new lambda value using the probability function from the slides with the other lambda and n0 fixed
    if(is1):
        # use data from 0 to n0
        return 1  # dummy placeholder
    else:
        # use data from n0 + 1 to N
        return 0


# initialize the number of iterations and the number of simulated points
Iterations = 10000
Points = 100
noFirst = 0 # initial value of n0 we decide for when it starts the montecarlo stuff

# Here we take in the data
gravData = 0 # replace zero with whatever data we get

# we then call the montecarlo function

n0, lambda1, lambda2 = montecarlogibbssampling(gravData, noFirst, Iterations, Points)

# We now have 3 lists of the 3 different values we are trying to find where each index corresponds to a specific
# simulated point. All we have left to do is graph the stuff.
