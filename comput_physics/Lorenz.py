from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#import numpy as np

x = [0.5]
y = [0.5]
z = [0.5]
n = 1
a = 10
b = 28
c = 8/3
t = 0.01
while n < 10000 :
        x_ = x[-1]
        y_ = y[-1]
        z_ = z[-1]
        x.append(x[-1]+(a*(y_-x_))*t)
        y.append(y[-1]+(b*x_-x_*z_-y_)*t)
        z.append(z[-1]+(x_*y_-c*z_)*t)
        n = n+1

ax = plt.subplot(111, projection='3d')    
ax.scatter(x, y, z, s=0.1)
plt.show()
