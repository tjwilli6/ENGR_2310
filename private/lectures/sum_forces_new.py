######################
#Author: T. Williamson
#Date: 2020-02-24
#sum_forces_new.py: A program to add two force vectors together
# user inputs |F| and theta in degrees for both forces
# program prints x and y components of Fsum


#Global constants
PI = 3.14

#Functions
def deg2rad(angle):
    """
    Convert an angle from degrees
    to radians
    """
    return angle * PI / 180

def factorial(number):
    """
    Calculate the factorial of number
    """
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
    main program
    """
    #Collect user input
    F1 = float(input("What is the magnitude of the first force (in Newtons)? "))
    theta1 = float(input("What is the angle of the first force (in deg)? "))
    F2 = float(input("What is the magnitude of the second force (in Newtons)? "))
    theta2 = float(input("What is the angle of the second force (in deg)?"))

    #Convert to radians
    theta1_rad = deg2rad(theta1)
    theta2_rad = deg2rad(theta2)

    #x and y components of Fsum
    F3x = F1 * cos(theta1_rad) + F2 * cos(theta2_rad)
    F3y = F1 * sin(theta1_rad) + F2 * sin(theta2_rad)


    print("Net force is: ",Fx3,Fy3)


#Now run the code!
main()
