from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
from pybrain.structure import FullConnection
from pybrain.structure import SigmoidLayer
from pybrain.structure import LinearLayer
import numpy as np
import matplotlib.pyplot as plt

TableZamena = []

ds = SupervisedDataSet(48, 26)
def make_data():

    trash = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    file = open('ABC_template.txt', 'r')
    number_of_line = 0
    counter = 0
    for line in file:

        if number_of_line%3 == 0 :

            lineElement = line.split(" ")

            trash[counter] = 1

            TableZamena.append(lineElement.pop(0))

            b = 0
            while b < len(lineElement):
                lineElement[b] = int(lineElement[b])
                b = b + 1

            ds.addSample(lineElement, trash)
            trash[counter] = 0

            counter = counter + 1
        number_of_line = number_of_line + 1

    file.close()

def indexMax(mass):
    i = 0
    index = 0
    max = mass[0]
    while i < len(mass):
        if max < mass[i]:
            index = i
            max = mass[i]
        i=i+1
    return index




def main():
    make_data()

    network = buildNetwork(48 , 26 )

    trainer = BackpropTrainer(network, ds)


    trainer.trainEpochs(500)

    counter = 0
    t = network.activate([1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,0,1,0,0,1,0,0,1,0])
    print TableZamena[indexMax(t)]


main()