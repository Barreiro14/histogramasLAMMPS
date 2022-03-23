import matplotlib.pyplot as plt


def his(timestep,thermo,np):
    step = timestep/thermo
    
    x = []
    y = []
    z = []
        
    f = open("posicion6.xyz","r")
    
    mylines = []
    for line in f:
        mylines.append(line)
    
    #print(mylines[1][17:])
    #print('Atoms. Timestep: {}'.format(timestep))
    #print(mylines[int(1 + (np+2)*i)][17:19])  
    
    init = 3 + np*step 
    ev = np + init
    i = init   
    
    k = 0
    while k < 3:  # this loop selects a k-column
        #print(mylines[i].split()[1])
        while i < ev: 
            #print(mylines[int(i)][0]) 
            if (mylines[int(i)][0]) == '2':    
                if k == 0:

                    x.append(float(mylines[int(i)].split()[1]))  
                    
                elif k == 1:
                    y.append(float(mylines[int(i)].split()[2]))  

                elif k == 2:
                    z.append(float(mylines[int(i)].split()[3]))  
   
                
            i = i + 1
        i = init    
        k = k + 1
    #print(x[0:100])
    #print(len(x)) 
    
    #print(len(x))
    #print(len(y))
    #print(len(z))

    
    #y_dict_x = {k:x.count(k) for k in x}
    #my_dict_y = {k:y.count(k) for k in y}
    #my_dict_z = {k:z.count(k) for k in z}

    plt.figure(figsize=(8,5)) 

    
    plt.hist(x,40,label='x')
    
    
    plt.hist(y,40,label = 'y')
    
    
    plt.hist(z,40,label = 'z')
    
    
    plt.xlabel('Posiciones')
    plt.legend(loc="upper left")
    #plt.bar(my_dict_x.keys(),my_dict_x.values(),width = 0.1)
    #plt.subplot(132)
    #plt.bar(my_dict_y.keys(),my_dict_y.values())
    #plt.subplot(133)
    #plt.bar(my_dict_z.keys(),my_dict_z.values())
    plt.grid(True) 
    plt.title('Histograma,step:{}'.format(timestep))
    plt.show() 

   
his(17000,100,11264)   