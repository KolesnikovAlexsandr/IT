
import neurolab as nl

import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

def make_data(Zamena , DataIn ):

    trash = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    file = open('ABC_template.txt', 'r')
    number_of_line = 0
    counter = 0
    for line in file:

        if number_of_line%3 == 0 :

            lineElement = line.split(" ")

            trash[counter] = 1

            Zamena.append(lineElement.pop(0)[0])

            b = 0
            while b < len(lineElement):
                lineElement[b] = int(lineElement[b])
                b = b + 1

            DataIn.append(lineElement)
            i = 0
            j = 0
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




def work(Data):
    trash = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0 , 0 , 0 , 0 , 0 , 0]
    file = open('Neural_network_homework.txt', 'r')
    counter = 0
    string  = ""
    for l in file:
        i = 0
        string = string + l
    string = string+"   "
    i = 0
    result = ""
    while i < len(string):
        if string[i] == "{":
            counter = 0
        elif string[i] == "1" or string[i] == "0":
            trash[counter] = int(string[i])
            counter = counter + 1
        elif string[i] == "}" or counter == 48:
            Data.append(trash)
            counter = 0
        elif string[i] == '"' and string[i+1] == " " and string[i+2] == '"':
            i=i+2

        i = i + 1

    print result

def main():
    TableZamena = []
    DataTrain = []
    DataOut = []
    make_data(TableZamena,DataTrain)

    DataTrain = np.asfarray(DataTrain)
    DataTrain[DataTrain == 0] = -1
    net = nl.net.newhop(DataTrain)
    DataOut = net.sim(DataTrain)
    DataWork = []
    #work( net , TableZamena , DataTrain , DataOut )
    j = 0
    while j < 26:
        out = net.sim([DataTrain[j]])
        print ((out[0] == DataOut[0]).all(), TableZamena[j], len(net.layers[0].outs))
        j=j+1
    work(DataWork)
    k = 0
    test = []
    result = ""
    print DataWork
    a = DataWork[0]
    trash = net.sim(a)
    test = np.asfarray(trash)
    test[test == 0] = -1
    while k < 26:
        if (test[0] == DataOut[j]).all():
            result = result + TableZamena[j]
            print result
        k=k+1




main()