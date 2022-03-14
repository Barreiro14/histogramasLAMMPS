
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from divv import i_his
x = []
my_dict = i_his()
#i_his()

# Fixing random state for reproducibility
np.random.seed(19680801)

HIST_BINS = list(my_dict.values())
HIST_BINS = np.linspace(0,15,15)
#print(HIST_BINS)

data = list(my_dict.values())
print(type(data[0]))
n,_= np.histogram(data, HIST_BINS)

def prepare_animation(bar_container):

    def animate(frame_number):
        # simulate new data coming in
        #data = np.random.randn(1000)
        
        n, _= np.histogram(data,HIST_BINS)
        for count, rect in zip(n, bar_container.patches):
            rect.set_height(count)
        return bar_container.patches
    return animate

fig, ax = plt.subplots()
_, _, bar_container = ax.hist(data, HIST_BINS, lw=1,
                              ec="yellow", fc="green", alpha=0.5)
ax.set_ylim(top=25)  # set safe limit to ensure that all data is visible.

ani = animation.FuncAnimation(fig, prepare_animation(bar_container), 50,
                              repeat=False, blit=True)
plt.show()
