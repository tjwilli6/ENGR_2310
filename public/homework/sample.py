#########################
#Author: Tyler Williamson
#Date: January 1, 1970
#sample.py: a brief program to illustrate
# readability and style guidlines for ENGR 2320


import math
import random

#Program-wide constants
PI = 3.14
#Euler's number
E = 2.72
#Newton's constant
G = 6.7e-11
#Coulomb's constant
K = 9e-9


#Function definitions
def grav_force(m1,m2,r):
    """
    Calculate the mutual gravitational force between 
    two point masses m1 and m2, separated by a distance r.
    Assume m1,m2 are given in kg, r in meters, returns Newtons
    """
    force = G * m1 * m2 / r**2

def elec_force(q1,q2,r):
    """
    Calculate the electric force between two point charges
    q1 and q2, separated by a distance r. q1,q2 should be 
    in Coulombs, r in meters. Returns Newtons.
    """
    force = k * q1 * q2 / r**2

def factorial(number):
    """
    Calculate the factorial of number
    """
    #Start at 1, then multiply by "number"
    # while decreasing number by 1 each
    result = 1
    while number > 0:
        result = result * number
        number = number - 1 #number-=1
    return number

def cos(x,num_of_terms=20):
    """
    Compute cos(x) using a Taylor expansion
    num_of_terms is an optional argument
    cos(x) ~= 1 - x**2/2! + x**4/4! - x**6/6! + ...
    """
    #loop counter
    n = 0
    #power each term is raised to
    exponent = 0
    #alternating sign
    sign = -1
    #variable to hold the sum
    total = 0
    while n < num_of_terms:
        #calculate factorial (used in denominator)
        fact = factorial(number)
        #sign alternates each term
        sign = -1 * sign
        #Find the value and add to total
        term_value = sign * x**exponent / fact
        total = total + term_value
        n = n + 1
        #Bump up by 2 so exp goes from 0,2,4,6,...
        exponent = exponent + 2
    return total


def sin(x,num_of_terms=20):
    """
    Compute sin(x) using a Taylor expansion
    num_of_terms is an optional argument
    sin(x) ~= x - x**3/3! + x**5/5! - x**7/7! +...
    """
    #loop counter
    n = 0
    #power each term is raised to
    exponent = 1
    #alternating sign
    sign = -1
    #sum
    total = 0
    while n < num_of_terms:
        #calculate factorial
        fact = factorial(number)
        #continually alternating sign
        sign = -1 * sign
        term_value = sign * x**exponent / fact
        total = total + term_value
        n = n + 1
        #Bump up by 2 so exp goes from 1,3,5,7...
        exponent = exponent + 2
    return total



def main():
    """
    Code within this function will be run when the file is invoked
    via Python (eg 'python3 sample.py')
    """
    print("This is the main program!")




#Call main() and run the program
main()
