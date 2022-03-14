import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Fixing random state for reproducibility
np.random.seed(19680801)

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
           # y.append(line[2])
            #z.append(line[3])
           #print()
    print(i)        

#i_his()
x = np.linspace(-4, 4, 100)
 #Numero de atomos tipo 2 (10% de las particulas totales) multiplicado por el max timestep
data = np.linspace(0,8000)
data = np.random.randn(1000)

#np.histogram(data, x)
# Esta parte la copie de https://matplotlib.org/3.5.1/gallery/animation/animated_histogram.html#sphx-glr-gallery-animation-animated-histogram-py
# Solo la modifique un poco 
nx, _ = np.histogram(data, x)
def prepare_animation(bar_container):
    def animate(frame_number):
        # simulate new data coming in
        data = np.random.randn(1000)
        nx, _ = np.histogram(data, x)
        #ny, _ = np.histogram(data,y)
        #nz, _ = np.histogram(data,z)

        for count, rect in zip(nx, bar_container.patches):
            rect.set_height(count)
        return bar_container.patches
    return animate



fig, ax = plt.subplots()
_, _, bar_container = ax.hist(data, nx, lw=1,
                              ec="yellow", fc="green", alpha=0.5)
ax.set_ylim(top=55)  # set safe limit to ensure that all data is visible.

ani = animation.FuncAnimation(fig, prepare_animation(bar_container), 50,
                              repeat=False, blit=True)
plt.show()


