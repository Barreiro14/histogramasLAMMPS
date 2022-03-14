
def i_his():
    file = open("posicion6.xyz", "r")
    
    x = [] 
    y = []
    cont = []
    
    for line in file:
        i = 0
        if (line[0] == '2'):
            
            #print(float(line[2:6]))
            x.append(float(line[2:6]))
           
    my_dict = {i:x.count(i) for i in x}               
                              
    return my_dict     
         
    
