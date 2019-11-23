import numpy as np
import matplotlib.pyplot as plt

N = 2060
p =0.5
bn = [p**(N-1000)]
an = [p**N]
x = np.arange(0, 2*N, 1)
for i in range(0, 2*N):
    b = bn[-1]
    bn.append(b*(N+i)/(i+1)*(1-p))
    an.append(bn[-1]*p**500)
    an[-1] = an[-1]*p**500

del(an[0])

a = 1/an[2058]
b = a/np.sqrt(2*np.pi)    #sigma
y = []
for i in x:
    y.append(1/a*np.exp(-(i-2058)**2/(2*b*b)))  #normaal distribution
    
plt.plot(x,y,'blue',label='Plate')
plt.plot(x,an,'orange',label='Normal')
plt.legend()
plt.show()
