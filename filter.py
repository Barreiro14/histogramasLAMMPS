# n es el numero de archivos: run/timestep 
# El timestep actual es de 100 (Se actualiza cada 100)
def filter(n):
	i = 0
	while i < n:
		f = open("fil_pos{i}".format(i),"a")
		fi = open("pos{i}".format(i),"r")
		for line in fi:
			if (line[0] == 2):
				f.write(line)
		i += 1		