

def timeStepFinder():
    file = open("posicion6.xyz", "r")
    i = 0
    for line in file:
        f = open("pos{}".format(i), "a")
        if line[0:5] == '11264': #number of atoms
            i = i + 1
            print("encontro la linea")
            #break
        else:
            #print(line[0:4])
            print(line)
            f.write(line)
            #f.write("")

