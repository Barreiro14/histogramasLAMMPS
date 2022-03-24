from timeStepFinder import timeStepFinder
from filter import filter 
from histograma_simple import his_simple

def main():
	print("hasta ahora todo jevi")
	#main function
	
	timeStepFinder() #puse 6 porque son 6 archivos que se pueden sacar con el actual loglammps (600/100)
	filter(8)
	his_simple(8)



if __name__ == '__main__':
	main()
