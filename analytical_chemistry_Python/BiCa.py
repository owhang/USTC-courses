import matplotlib.pyplot as plt
import numpy as np

K1 = 4.9*10**10/(10**18.01)
K2 = 8.7*10**27/(10**18.01)
Vmin = 0
Vmax = 40

py = np.linspace(-20,-2, 100000)
y_ = []
V = []
pBi = []

for i in py:
    y_.append(10**i)
    y = y_[-1]
    V.append((0.2*K1*y/(1+K1*y)+0.38*K2*y/(1+K2*y)+80*y)/(0.02-y))
    pBi.append(-np.log10(0.38/(V[-1]+80)/(1+K2*y)))

def pfind(x, x0):
    for i in range(0, len(x)):
        if x[i] >= x0:
            return i
    print("No result!")

print("pBi: ",pBi[pfind(V, 19.00)])
print("Et2: ", (V[pfind(pBi, 4.0)]/19-1)*100)
print("pBiJump: ", pBi[pfind(V, 18.981)], pBi[pfind(V, 19.019)])

plt.plot(V, pBi,'black', label="pBi-V")
plt.xlim(Vmin, Vmax)
plt.xlabel('$V$/mL')
plt.ylabel("$pBi$")
plt.legend()
plt.show()
