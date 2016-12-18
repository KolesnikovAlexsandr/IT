
import neurolab as nl

import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

def make_data( Zamena , DataIn ):

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

def indexMax(DataIn , DataOut):
    mass = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    k = 0
    while k < 26:
        counter = 0
        j = 0
        while j < 46:
            j = j+1
            if DataIn[k][j] == DataOut[j]:
                counter = counter +1
        mass[k] = counter
        k = k+1
    i = 0
    index = 0
    max = mass[0]
    while i < len(mass):
        if max < mass[i]:
            index = i
            max = mass[i]
        i=i+1
    return index




def work( DataOut , TableZamena):
    trash = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0 , 0 , 0 , 0 , 0 , 0]

    file = open('Neural_network_homework.txt', 'r')
    counter = 0
    string  = ""
    for l in file:
        string = string + l

    string = string+"   "
    i = 0
    result = ""
    while i < len( string ):
        if string[ i ] == "{":
            counter = 0
        elif string[ i ] == "1" or string[ i ] == "0":
            trash[ counter ] = int( string[ i ] )
            counter = counter + 1
        elif string[ i ] == "}" or counter == 48:
            result = result + TableZamena[indexMax(DataOut,trash)]
            counter = 0
        elif string[ i ] == '"' and string[ i + 1 ] == " " and string[ i + 2 ] == '"':
            result = result + " "
            i = i + 2
        elif string[ i ] == '"' and string[ i + 1 ] == "," and (string[ i + 2 ] == ' ' or string[ i+2 ] == '"'):
            result = result + ","
            i = i + 3
        i = i + 1
    print "Message:"
    print result





def main():
    TableZamena = []
    DataTrain = []
    make_data(TableZamena , DataTrain)
    work( DataTrain , TableZamena)














main()


