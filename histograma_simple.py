import matplotlib.pyplot as plt
import numpy as np

def his_simple(n):
    i = 0

    while i < n:
        x = []
        y = []
        z = []
        
        ff = open("fil_pos{}".format(0),"r")
        for line in ff:
            x.append(float(line[2:6]))
            #y.append(float(line[10:14]))
            #z.append(float(line[18:22]))
        
        my_dict_x = {k:x.count(k) for k in x}
        #my_dict_y = {k:y.count(k) for k in y}
        #my_dict_z = {k:z.count(k) for k in z}
        
        plt.bar(my_dict_x.key(),my_dict_x.values())
        plt.show()
        
