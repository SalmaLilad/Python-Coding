def consultants_fee(t):
    if t <= 5:
        fee = 50
    elif t <= 15:
        fee = 60
    else:
        fee = 100 + 10 * (t - 15)
        
    return fee

import numpy as np
import matplotlib.pyplot as plt
time_range = range(0,60,1)
fee = np.vectorize(consultants_fee)(time_range)
plt.scatter(time_range,fee)
plt.xlabel("Time (minutes)")
plt.ylabel("Consultant's fee (Dollars)")
plt.grid('on')
