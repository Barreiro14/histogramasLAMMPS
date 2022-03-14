
def i_his():
    file = open("posicion6.xyz", "r")
    filx = open("posicion6.xyz", "r")
    x = [] 
    y = []
    cont = []
    i = 0 
    for line in file:
       
        if (line[0] == '2'):
            i = 0
            #print(float(line[2:6]))
            x.append(float(line[2:6]))
            #print(x)
            y = line[2:6]
            
            for lin in filx:
                #x.append(float(line[2:6]))
                if lin[2:6] == y:
                   i += 1
            cont.append(i)    
           
    print(cont)        

i_his()