import numpy as np
import scipy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
     
def dY_dt(Y,t):
    a = 1.0
    b = 0.2
    d0=a*(Y[0]-(Y[0]*Y[1]))
    d1=b*(-Y[1]+(Y[0]*Y[1]))
    return [d0,d1]
 
#initial condition of y0 and y1                           
Y=np.array([0.10, 1.0])   
# partition the time from t = 0 to 5 into 100 uniform partition              
t=np.linspace(0, 5, 100)
y= sp.integrate.odeint(dY_dt,Y,t)

# plot the graph for both y0 and y1 against t
fig1=plt.figure()
ax1=fig1.add_subplot(111)
ax1.plot(t, y)
plt.xlabel("Year (t)")
plt.ylabel("Prey-Predator(y) ");
plt.plot(t, y[:,0], label='prey', color="b")
plt.plot(t, y[:,1], label='predator', color="r")
plt.title('Prey-Predator against Year')
plt.savefig("Graph of Prey-Predator against Year")
plt.grid()
plt.show()

fig2=plt.figure()
ax2=fig2.add_subplot(111)
ax2.plot(y[:,0], y[:,1])
plt.xlabel("Prey (y0)")
plt.ylabel("Predator (y1)");
plt.title('Predator against Prey')
plt.savefig("Graph of Predator against Prey")
plt.grid()
plt.show()

#sensitivity with y0=0.11                      
Y2=np.array([0.11,1.0])                 
t=np.linspace(0, 5, 100)
y2= sp.integrate.odeint(dY_dt,Y2,t)

fig3=plt.figure()
ax3=fig3.add_subplot(111)
ax3.plot(t, y2)
plt.xlabel("Year (t) ")
plt.ylabel("Prey-Predator(y) ");
plt.plot(t, y2[:,0], label='prey', color="b")
plt.plot(t, y2[:,1], label='predator', color="r")
plt.title('Prey-Predator against Year(2)')
plt.savefig("Graph of Prey-Predator against Year(2)")
plt.grid()
plt.show()

fig4=plt.figure()
ax4=fig4.add_subplot(111)
ax4.plot(y2[:,0], y2[:,1])
plt.xlabel("Prey (y0)")
plt.ylabel("Predator (y1)");
plt.title('Predator against Prey(2)')
plt.savefig("Graph of Predator against Prey(2)")
plt.grid()
plt.show()
