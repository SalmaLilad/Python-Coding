import numpy as np
def wingy_function(theta):
    r = np.exp(np.cos(theta)) - 2 * np.cos(4 * theta) + (np.sin(theta/12))**5
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    return x, y

import matplotlib.pyplot as plt
def draw_wingy(num_revolutions):
    theta = np.linspace(0 * np.pi, num_revolutions * 2*np.pi, 1000)
    x, y = wingy_function(theta)
    plt.plot(x, y, color = 'green') 
    plt.axis('equal')
    plt.title('number of revolutions = ' + str(num_revolutions))  
    
num_revolutions = 6 # try 2, 4, 6, 12, 20 or any other not too large integer 
draw_wingy(num_revolutions)
