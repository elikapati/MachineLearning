from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

fig = plt.figure()
style.use('fivethirtyeight')
ax1 = fig.add_subplot(111, projection='3d')

# Part - I
# --------
x1 = [1,2,3,4,5,6,7,8,9,10]
y1 = [5,6,4,3,5,6,3,5,5,2]
z1 = [1,2,4,6,7,3,5,6,6,9]
#ax1.plot(x1, y1, z1, c = 'g', marker = 'o')

# Part - II
# ---------
x2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y2 = [-5,-6,-4,-3,-5,-6,-3,-5,-5,-2]
z2 = [1,2,4,6,7,3,5,6,6,9]
#ax1.scatter(x1, x2, z2, c = 'r', marker = 'o')
#ax1.scatter(x2, y2, z2, c = 'b', marker = 'o')

# Part - III
# ----------
# 3d bars
x3 = [1,2,3,4,5,6,7,8,9,10]
y3 = [5,6,4,3,5,6,3,5,5,2]
z3 = [1,2,4,6,7,3,5,6,6,9]

dx = np.ones(10)
dy = np.ones(10)
dz = [1,2,3,4,5,6,7,8,9,10]

ax1.bar3d(x3, y3, z3, dx, dy, dz)

# Part - IV Wireframe
# ---------
x, y, z = axes3d.get_test_data()
print(axes3d.__file__)

ax1.plot_wireframe(x, y, z, rstride=4, cstride=4 )

ax1.set_xlabel('x axis')
ax1.set_xlabel('y axis')
ax1.set_xlabel('z axis')

plt.show()