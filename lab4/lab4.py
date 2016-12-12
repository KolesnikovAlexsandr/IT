from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
from pybrain.structure import FullConnection
from pybrain.structure import SigmoidLayer
from pybrain.structure import LinearLayer
import webbrowser
import speech_recognition as sr

import numpy as np
import matplotlib.pyplot as plt

TableZamena = []

ds = SupervisedDataSet(48, 26)

network = buildNetwork(48 , 26 )
def make_data():

    trash = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    file = open('ABC_template.txt', 'r')
    number_of_line = 0
    counter = 0
    for line in file:

        if number_of_line%3 == 0 :

            lineElement = line.split(" ")

            trash[counter] = 1

            TableZamena.append(lineElement.pop(0)[0])

            b = 0
            while b < len(lineElement):
                lineElement[b] = int(lineElement[b])
                b = b + 1

            ds.addSample(lineElement, trash)
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




def trainNetworck():
    trainer = BackpropTrainer(network, ds)
    trainer.trainUntilConvergence()


def work():
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
            #print network.activate(trash)
            result = result + TableZamena[indexMax(network.activate(trash))]
            counter = 0
        elif string[i] == '"' and string[i+1] == " " and string[i+2] == '"':
            result = result + " "
            i=i+2

        i = i + 1

    print result

def main():
    '''make_data()
    trainNetworck()
    trash = [1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1]
    print TableZamena[indexMax(network.activate(trash))] #E
    trash = [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,1,1,1,0,1]
    print TableZamena[indexMax(network.activate(trash))]
    trash = [1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0]
    print TableZamena[indexMax(network.activate(trash))]#T
    work()
    Chrome = webbrowser.MacOSX('default')
    url = 'http://www.vk.com/'
    Chrome.open_new_tab(url)'''


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

# Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))



main()