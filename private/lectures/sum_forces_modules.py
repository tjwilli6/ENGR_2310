######################
#Author: T. Williamson
#Date: 2020-02-24
#sum_forces_new.py: A program to add two force vectors together
# user inputs |F| and theta in degrees for both forces
# program prints x and y components of Fsum

import functions


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
    theta1_rad = functions.deg2rad(theta1)
    theta2_rad = functions.deg2rad(theta2)

    #x and y components of Fsum
    F3x = F1 * functions.cos(theta1_rad) + F2 * functions.cos(theta2_rad)
    F3y = F1 * functions.sin(theta1_rad) + F2 * functions.sin(theta2_rad)


    print("Net force is: ",F3x,F3y)


#Now run the code!
main()
