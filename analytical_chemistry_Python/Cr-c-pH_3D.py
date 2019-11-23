import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

K1 = 10**6.49
K2 = 10**7.23
K3 = 10**14.69
pH0 = np.arange(-2,14,0.1)
c0  = np.arange(0.1, 6, 0.1)
pH, c = np.meshgrid(pH0, c0)
H = 10**(-pH)
a = 2*K3*H**2
b = K1*H + K2*H**2 +1
Cr3 = (-b+np.sqrt(b**2+4*a*c))/(2*a)
#Cr1 = K2*H*H*Cr3
Cr2 = K1*H*Cr3
#Cr4 = 2*K3*H*H*Cr3*Cr3


fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(pH, c, Cr2/c,rstride=1, cstride=1, cmap='rainbow')
ax.set_xlabel('pH')
ax.set_ylabel('$c$/mol∙L$^{-1}$')
ax.set_zlabel('$\mathrm{\delta}$')
ax.set_zlim(0,1)
#ax.set_title('$\mathrm{\delta(H_{2}CrO_{4})}$')     #Cr1
ax.set_title('$\mathrm{\delta(HCrO_{4}^{-})}$')     #Cr2
#ax.set_title('$\mathrm{\delta(CrO_{4}^{2-})}$')     #Cr3
#ax.set_title('$\mathrm{\delta(Cr_{2}O_{7}^{2-})}$')  #Cr4
plt.show()
