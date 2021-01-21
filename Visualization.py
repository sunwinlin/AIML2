import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
x=np.linspace(-2*np.pi, 2*np.pi,100)
sinx=np.sin(x)
plt.plot(x,sinx, label='sin')
plt.legend(loc="best")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid()
plt.show()