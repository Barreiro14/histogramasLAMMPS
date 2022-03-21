

def timeStepFinder():
    file = open("posicion6.xyz", "r")
    i = 0
    
    
    for line in file:
        f = open("pos{}".format(i), "a")
        if line[0:4] == '11264': #number of atoms
            i = i + 1
            break
            
        else:
            f.write(line)
            f.write("")

