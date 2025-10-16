import numpy as n
def woozy_function(theta):
    r = theta
    x = r * n.cos(theta)
    y = r * n.sin(theta)
    return x, y 

import matplotlib.pyplot as plt
def draw_woozy(turns):
    theta = np.linspace(0 * np.pi, turns * np.pi, 1000)
    x, y = woozy_function(theta)
    plt.plot(x,y)
    plt.axis('equal')
    plt.title('turns  = ' + str(turns))
    
turns = 32 # try 16, 32, 64
draw_woozy(turns)
