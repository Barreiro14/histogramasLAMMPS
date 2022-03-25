import matplotlib.pyplot as plt
import numpy as np

def his_simple(n):
    i = 1

    while i < n:
        ff = open("fil_pos{}".format(i), "r")
        f = ff.read()
        h = np.empty(len(f))
        j = 0
        #print(len(f))
        for line in ff:
            h[j] = float(line[2:6])
            j = j + 1
            #h = np.append(h, float(line[2:6]))
            #print(line)
            #print((f))
            #print(h)
            #print(float(line[2:6]))
            #print(i)
            #print(h)
        #print(h[-1])
        plt.hist(h, 50)
        plt.show()
        #plt.hist(h)
        #plt.show()
        i = i + 1
    #plt.show()
        
