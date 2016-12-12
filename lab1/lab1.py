from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.supervised.trainers import Trainer
from pybrain.datasets import SupervisedDataSet
from pybrain.structure import GaussianLayer
from pybrain.structure import FullConnection
from pybrain.structure import LinearLayer

import numpy as np
import matplotlib.pyplot as plt


def x_3(x):
    return x*x*x


def main():
    i = -1
    x = [ ]
    y = [ ]
    y_out = []
    ds = SupervisedDataSet(1, 1)
    while i < 1:
        x.append( i )
        y.append(x_3( i ))
        i = i + 0.1
        ds.addSample(i,x_3(i))


    network = buildNetwork(1 ,1, 1, bias=True , recurrent=True  ,outclass=LinearLayer )
    recCon = FullConnection(network['out'], network['hidden0'])
    network.addRecurrentConnection(recCon)
    network.sortModules()

    trainer = BackpropTrainer(network, ds,learningrate=0.05)
    #trainer = Trainer(network , ds , learningrate=0.06)


    trainer.trainUntilConvergence()

    i = -1
    while i < 1:
        a = network.activate([i])
        print a
        print i
        y_out.append(a)
        i = i + 0.1

    plt.plot(x, y, 'b', y_out , y ,  'r')
    plt.show()



main()
