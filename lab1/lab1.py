from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
import numpy

def x_3(x):
    return x*x*x


def main():
    i = 0
    x = [ ]
    y = [ ]
    y_out = []
    ds = SupervisedDataSet(1, 1)
    while i < 0.5:
        x.append( i )
        y.append(x_3( i ))
        i = i + 0.1
        ds.addSample(x[x.len],y[y.len])
    network = buildNetwork(1, 1, 1)

    print x
    print y



main()
