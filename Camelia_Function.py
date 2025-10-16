import numpy as np
def camelia_function(theta):
    r = theta + 2 * np.sin(2*np.pi*theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

import matplotlib.pyplot as plt
def draw_camelia(turns):
    theta = np.linspace(0 * np.pi, turns * np.pi, 1000)
    x,y = camelia_function(theta)
    plt.plot(x, y, color = 'pink')
    plt.axis('equal')
    plt.title('turns  = ' + str(turns))

turns = 16 # try 16, 32, 64 or any other integer
draw_camelia(turns)

camelia_turns = 16 # enter the numerical value based on your experimentation 
draw_camelia(camelia_turns)
