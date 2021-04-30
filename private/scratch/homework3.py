# Cameron Stanley
# 4-16-2021
# In this program it asks sigma and the number of rectangles you would like to use. then it will calculate the moment of inertia for a thin metal rod.
# Then it will print the Riemann estimate of I togrther and the uncertainty on the estimate.
 
import numpy as np

def function_one(x):
    return (x**2) * np.exp((-1/2)*((x/sigma)**2))

def function_one_deriv(x):
    return (((x**3)*np.exp(-(x**2)/(2 * (sigma**2))))/(2 * sigma))+(2*x*np.exp(-(x**2)/(2 * (sigma**2))))

def function_two(x):
    return np.exp((-1/2)*((x/sigma)**2))

def function_two_deriv(x):
    return (np.exp(-(x**2)/(2 * (sigma**2))))/(2 * sigma)

# The intergation of the first Function.
def integration_F1(xi,xf,n):
    dx = (xf - xi)/n
    total1 = 0
    i = 0
    for i in range(n):
        x = xi + i * dx
        f = function_one(x)
        area = f * dx
        total1 += area
    return total1

# The integration of the second Function.
def integration_F2(xi,xf,n):
    dx = (xf - xi)/n
    total2 = 0
    i = 0
    for i in range(n):
        x = xi + i * dx
        f = function_two(x)
        area = f * dx
        total2 += area
    return total2

# The uncertainty of the inegration of first function.
def uncertainty_F1(xi,xf,n):
    x = np.linspace(xi,xf,n)
    dxdt_1 = function_one_deriv(x)
    M1 = dxdt_1.max()
    return (1/2) * M1 * (((xf - xi)**2)/n)

# The uncertainty of the inegration of second function.
def uncertainty_F2(xi,xf,n):
    x = np.linspace(xi,xf,n)
    dxdt_2 = function_two_deriv(x)
    M2 = dxdt_2.max()
    return (1/2) * M2 * (((xf - xi)**2)/n)

# The Inertia calculation.
def inertia(M):
    return M * (integration_F1(xi, xf, n)/integration_F2(xi,xf,n))

# The uncertainty of the inertia calculation.
def uncert_inertia(M):
    return M * ((uncertainty_F1(xi,xf,n)/integration_F1(xi,xf,n))+(uncertainty_F2(xi,xf,n)/integration_F2(xi,xf,n)))* inertia(M)
# The global variables.
M = 1
L = 1
# The xi and xf are like this so that if you need to change the range of intagration. You can do it very easy with just changing to lines of code.
xi = -L/2
xf = L/2
# This part asks the user what the value of sigma and the number of recangles the user would like. 
sigma = float(input('What is the value of sigma you would like: '))
n = int(input('How many rectangles would you like: '))
# main function. I calls all the other functions and calculates the inertia and the uncertainty. Then it prints those numbers.
def main():
    c = inertia(M)
    u = uncert_inertia(M)
    print("the inertia for the rod is",c,"and the uncertainty is",u)

main()
