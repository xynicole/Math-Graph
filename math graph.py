'''
Xinyi Huang
MATH 323

'''

from mpl_toolkits.mplot3d import Axes3D  

import numpy as np
import matplotlib.pyplot as plt



'''
toroidal spiral
'''

t = np.linspace(2, 30, 8000)

x = (4 + np.sin(20*t))*np.cos(t)
y = (4 + np.sin(20*t))*np.sin(t)
z = np.cos(20*t)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(x, y, z, label='toroidal spiral')
ax.legend()

plt.show()


'''
trefoil knot
'''

t = np.linspace(6, 25, 800)

x = (2 + np.cos(1.5*t))*np.cos(t)
y = (2 + np.cos(1.5*t))*np.sin(t)
z = np.sin(1.5*t)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(x, y, z, label='trefoil knot')
ax.legend()

plt.show()
