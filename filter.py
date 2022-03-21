# n es el numero de archivos: run/timestep 
# El timestep actual es de 100 (Se actualiza cada 100)
def filter(n):
	i = 0
	while i < n:
		fi = open("fil_pos{}".format(i),"a")
		f = open("pos{}".format(i),"r")
		for line in f:
			if (line[0] == '2'):
				fi.write(line)
		i += 1		