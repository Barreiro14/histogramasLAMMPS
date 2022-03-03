file = open("position.xyz", "r")

def timeStepFinder():
    i = 0
    f = open("pos{i}".format(i), "a")
    for line in file:
        if line == 1000: #number of atoms
            i = i + 1
            break
        else:
            f.write(line)
            f.write("")

