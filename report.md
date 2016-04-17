UECM3033 Assignment #3 Report
========================================================

- Prepared by: ** Yang Guang Tosng **
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  Gauss-Legendre formula

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/tiago5829/UECM3033_assign3](https://github.com/your_github_id/UECM3033_assign3)


Explain how you implement your `task1.py` here.

First of all, we imported the numpy and sympy as np and sy respectively. We used function gausslegendre,in order to implement the N-point Gauss-Legendre quadrature,use the polynomial.legendre.leggauss to compute the sample points for Gauss-Legendre quadrature. The default interval for Gauss-Legendre quadrature is [-1,1]. For the interval,we use t =0.5(x+1)(b-a)+a to change from [-1,1] to [a,b] . Then the answer return to gausslegendre function will be the multiplication of the sum of (w*f(t)) and half of the difference of upper and lower limit.

In the main function, the self-defined function named my_integral will return answer for integration. Lastly, we used answer of my_integral to compare as the answer returned by gausslegendre, which I=0.400338097411

Explain how you get the weights and nodes used in the Gauss-Legendre quadrature.

The weights and nodes can be get by importing numpy.polynomial.legendre.leggauss.

---------------------------------------------------------

## Task 2 -- Predator-prey model

Explain how you implement your `task2.py` here, especially how to use `odeint`.

First of all, we imported numpy, scipy and matplotlib.pyplot as np,sp and plt respectively. Then, we created a self-defined function named dY_dt which will assign the upper limit,b and lower limit,a for the integral and return the differential equations of prey and predator.an array with initial condition was created which was when x is 0, the y will be 0.1 and 1.0 respectively. Then, the time which was 0 to 5 years were chopped into 1000 sections by using np.linspace(0,5,100). Then , uesd use function integrate.odeint in scipy to integrate the system of ordinary differential equations with input dY_dt, array Y and t.by the help of matplotlib.pyplot, the graph of Prey-Predator against Year and graph of predator against prey also can be created. Then, for the second part, the initial condition was modified where the array will becme 0.11 and 1.0 while others will remain the same.

Put your graphs here and explain.

When the y0 is 0.1, y1 is 1.0.

![Graph of Prey-Predator against Year.png](Graph of Prey-Predator against Year.png)
![Graph of Predator against Prey.png](Graph of Predator against Prey.png)

When the y0 is 0.11, y1 is 1.0.

![Graph of Prey-Predator against Year(2).png](Graph of Prey-Predator against Year(2).png)
![Graph of Predator against Prey(2).png](Graph of Predator against Prey(2).png)

At first, the population or number of prey is the lowest while the number of predators is the highest. The predator decrease because the prey(food) is lesser, so the prey able to increase their population. As the time increases, the population or number of prey will increases over time as the number of predators is decreasing. Red colour indicates the predator and Blue colour indicates the prey.

Is the system of ODE sensitive to initial condition? Explain.

In my opinion, the difference between the both graph of y0=0.1 and y0=0.11 is not very obvious,hence it is assume thet the system of ODE is not sensitive to initial condition. If the ODE system is sensitive, a minor change in the initial value will cause a obvious change in the graph.

-----------------------------------

<sup>last modified: change your date here</sup>
