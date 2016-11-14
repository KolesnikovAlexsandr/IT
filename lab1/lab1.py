from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
from pybrain.structure import FullConnection
from pybrain.structure import SigmoidLayer
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
        i = i + 0.01
        ds.addSample(i,x_3(i))

    network = buildNetwork(1 ,1, 1, bias=True , recurrent=True , hiddenclass=SigmoidLayer)
    recCon = FullConnection(network['in'], network['hidden0'])
    network.addConnection(recCon)
    network.sortModules()

    print network['in']
    print network['hidden0']
    print network['out']
    trainer = BackpropTrainer(network, ds,learningrate=0.05)


    trainer.trainEpochs(1000)

    print network.activate([0])

    plt.plot(x,y)
    plt.show()



main()
