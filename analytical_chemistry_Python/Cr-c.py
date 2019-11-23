import matplotlib.pyplot as plt
import numpy as np

K1 = 10**6.49
K2 = 10**7.23
K3 = 10**14.69
C = np.linspace(0.001,6,10000)
h = 10**(-7)
A, B, Cr1, Cr2, Cr3, Cr4 = [], [], [], [], [], []

for c in C:
    A.append(2*K3*h*h)
    B.append(K1*h+K2*h*h+1)
    a, b =A[-1], B[-1] 
    Cr3.append((-b+np.sqrt(b*b+4*a*c))/(2*a))
    cr = Cr3[-1]
    Cr1.append(K2*h*h*cr)
    Cr2.append(K1*h*cr)
    Cr4.append(2*K3*h*h*cr*cr)

plt.xlim(0,6)
plt.ylim(-0.01,1)    
plt.plot(C, Cr1/C, label="$\mathrm{H_{2}CrO_{4}}$")
plt.plot(C, Cr2/C, label="$\mathrm{HCrO_{4}^{-}}$")
plt.plot(C, Cr3/C, label="$\mathrm{CrO_{4}^{2-}}$")
plt.plot(C, Cr4/C, label="$\mathrm{Cr_{2}O_{7}^{2-}}$")
plt.xlabel("$c$/mol∙L$^{-1}$")
plt.ylabel("$\delta$")
plt.legend()
plt.show()
