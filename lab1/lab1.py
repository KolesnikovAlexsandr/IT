import pybrain
import numpy

def x_3(x):
    return x*x*x


def main():
    i = -1
    x = [ ]
    y = [ ]

    while i < 1:
        x.append( i )
        y.append(x_3( i ))
        i = i + 0.1
        
    print x
    print y



main()
