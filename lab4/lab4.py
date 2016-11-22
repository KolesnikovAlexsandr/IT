from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
from pybrain.structure import FullConnection
from pybrain.structure import LinearLayer
import numpy as np
import matplotlib.pyplot as plt



def main():
    f = open('ABC_template.txt', 'r')
    ds = SupervisedDataSet(1, 1)
    ds.addSample()


    network = buildNetwork(1 ,1, 1, bias=True , recurrent=True ,hiddenclass=LinearLayer )
    recCon = FullConnection(network['in'], network['hidden0'])
    network.addConnection(recCon)
    network.sortModules()

    trainer = BackpropTrainer(network, ds,learningrate=0.05)


    trainer.trainEpochs(1000)


main()