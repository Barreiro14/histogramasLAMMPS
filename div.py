x = []
y = []
z = []
file = open("posicion6.xyz", "r")
def i_his():   
    i = 0 
    for line in file:
       
        if (line[0] == '2'):
            i += 1
            print(float(line[2:6]))
            x.append(float(line[2:6]))
            y.append(line[10:14])
            z.append(line[18:])
           
    print(i)        
