import matplotlib.pyplot as plt
import numpy as np


K1 = 10**6.49
K2 = 10**7.23
K3 = 10**14.69
pH = np.linspace(-2,14,10000)
H, A, B, Cr1, Cr2, Cr3, Cr4 = [], [], [], [], [], [], []

for i in pH:
    H.append(10**(-i))
    h = H[-1]
    A.append(2*K3*h*h)
    B.append(K1*h+K2*h*h+1)
    a, b =A[-1], B[-1] 
    Cr3.append((-b+np.sqrt(b*b+4*a))/(2*a))
    cr = Cr3[-1]
    Cr1.append(K2*h*h*cr)
    Cr2.append(K1*h*cr)
    Cr4.append(2*K3*h*h*cr*cr)

plt.xlim(-2,14)
plt.ylim(0,1)    
plt.plot(pH, Cr1, label="$\mathrm{H_{2}CrO_{4}}$")
plt.plot(pH, Cr2, label="$\mathrm{HCrO_{4}^{-}}$")
plt.plot(pH, Cr3, label="$\mathrm{CrO_{4}^{2-}}$")
plt.plot(pH, Cr4, label="$\mathrm{Cr_{2}O_{7}^{2-}}$")
plt.xlabel("pH")
plt.ylabel("$\delta$")
plt.legend()
plt.show()
