# Cameron Stanley
#  2-12-2021
# This code askes for the a, b, and c values and uses them to calculate x value for you.

a= float(input("Enter A for the formula: "))# inputs for the equation
b= float(input("Enter B for the formula: "))
c= float(input("Enter C for the formula: "))

def solve_quadratic(a,b,c):# is the function
    math = (b**2) - (4*a*c)
    linear = -c/b
    if a == 0:# if the a is less to zero then it does the linear equation becuase you cant have zero in the denomenator.
        print("x = ", linear)
    elif math < 0: # if the math equation is less then 0 it does this elif statment. The reason is you cant have a negative under a square root.
        print("The problem is to complex for the program. Sorry ")
    else:
        quadratic1 = (-b+ (((b**2)-(4*a*c))**(1/2)))/ (2*a)# quadratic equation
        quadratic2 = (-b- (((b**2)-(4*a*c))**(1/2)))/ (2*a)
        print("x equals both ", quadratic1,",", quadratic2)

solve_quadratic(a,b,c)
