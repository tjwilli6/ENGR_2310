# Cameron Stanley
#2/26/2021
#This code will caculate the area of one rectangle then calculate another rectangle.
# Then it will tell you if the two retangle are equall in area or not. 

x1= float(input("What is the length of the first rectangle: "))# the inputs for the area equations.
y1= float(input("What is the width of the first rectangle: "))
x2= float(input("What is the length of the second rectangle: "))
y2= float(input("What is the width of the second rectangle: "))
eps = 1e-5
import math#imports the math file

R1 = x1*y1#the area equations for the two rectangles.
R2 = x2*y2

if math.fabs(R1-R2) < eps:#the statment that tells you if the area are equall or not.
    print("The areas are equal")

else:
    print("The areas are not equal")
