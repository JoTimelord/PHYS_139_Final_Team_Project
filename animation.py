import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Final2V2
import numpy as np

n0 = Final2V2.n0
l1 = Final2V2.lambda1
l2 = Final2V2.lambda2


def update(t):
    ax.cla()

    x = l1[:t]
    y = l2[:t]
    z = n0[:t] + 2017

    ax.scatter(x, y, z, s = 5, marker = 'o')
    ax.scatter(Final2V2.lambda1_mean, Final2V2.lambda2_mean, Final2V2.n0_mean+2017, s=20,color = 'red')

    ax.set_xlim(5,25)
    ax.set_ylim(5,25)
    ax.set_zlim(80+2017,100+2017)
    ax.set_title('Simulation \nsteps = ' + str(t))



fig = plt.figure(dpi=100)
ax = fig.add_subplot(projection='3d')


ani = FuncAnimation(fig = fig, func = update, frames = 100, interval = 300)

ani.save("scatter.gif")