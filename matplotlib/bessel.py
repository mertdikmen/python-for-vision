from scipy import optimize, special
from numpy import *
import matplotlib.pyplot as plt
plt.ion()

x = arange(0,10,0.01)

for k in arange(0.5,5.5):
     y = special.jv(k,x)
     plt.plot(x,y)
     f = lambda x: -special.jv(k,x)
     #x_max = optimize.fminbound(f,0,10)
     x_max = optimize.fmin_bfgs(f,1.0)
     plt.plot([x_max], [special.jv(k,x_max)],'ro')

plt.title('Different Bessel functions and their local maxima')
plt.grid()


