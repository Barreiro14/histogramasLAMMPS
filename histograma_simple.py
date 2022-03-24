import matplotlib.pyplot as plt
import numpy as np

def his_simple(n):
    i = 0

    while i < n:
        x = []
        #y = []
        #z = []
        
        ff = open("fil_pos{}".format(i), "r")
        for line in ff:
            x.append(float(line[2:6]))
        i = i + 1
        plt.hist(x)
        plt.savefig("{}th time step".format(i*100))
    plt.show()
        
