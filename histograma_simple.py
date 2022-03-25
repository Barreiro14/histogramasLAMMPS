import matplotlib.pyplot as plt
import numpy as np

def his_simple(n):
    i = 0

    while i < n:
        h = []
        ff = open("fil_pos{}".format(i), "r")
        for line in ff:
            h.append(float(line[2:6]))
        i = i + 1
        plt.hist(h, 50)
        #plt.show()
        #plt.savefig("{}th time step.png".format(i*100))
        print(i)
        print(h)
    #plt.show()
        
