import neurolab as nl

import numpy as np
import matplotlib.pyplot as plt
import pylab as pl


def x_3(x):
    return x*x*x


def main():
    i = -1
    x = [ ]
    y = [ ]
    y_out = []

    x = np.linspace(-0.5, 0.5, 100).reshape(100, 1)
    y = x_3(x)

    networck = nl.net.newff([[-10, 10]], [5, 1])
    networck.train( x, y, epochs=500, show=100, goal=0.01)

    inp_test = np.linspace(-1.0, 1.0, 200).reshape(200, 1)
    out_test = networck.sim(inp_test).flatten()


    plt.plot(x, y, 'b',inp_test,out_test,'r')
    plt.show()



main()
