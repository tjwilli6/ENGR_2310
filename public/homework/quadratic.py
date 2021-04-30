###########################
# Author: Tyler Williamson
# Date:   02/05/2021                      
# quadratic.py: a program to calculate the roots of
# a quadratic equation


#Tell the user what to do
print("Enter the coefficients 'a', 'b', and 'c'",end='')
print(" of the polynomial 'ax^2+bx+c'",end='')
print(" and I will find the roots!")

#Collect coefficients from user
a = float(input("Enter coefficient 'a': "))
b = float(input("Enter coefficient 'b': "))
c = float(input("Enter coefficient 'c': "))


if a != 0:
    #If 'a' is not zero, two possibilities
    #discriminant >=0 --> use quadratic formula
    #discriminant < 0 --> complex, don't solve

    #Calculate discriminant
    disc = b**2 - 4 * a * c
    if disc >= 0:
        x1 = (-b + disc**0.5) / 2 / a
        x2 = (-b - disc**0.5) / 2 / a
        print("x1,x2 = (",x1,",",x2,")")
    else:
        print("The solution is complex, that's above my pay grade!")

else:
    #if a = 0, the equation is just bx+c=0-->x=-c/b

    #I said you could assume 'b' is not zero
    #If that wasn't the case, you have to check

    #'b' evaluates to True UNLESS it is zero
    if b:
        x = -c / b
        print("x = ",x)
    else:
        print("Nothing to solve for!")








    
    
