#Cameron Stanley
#2-26-2021
# This code will take the magnitude and angle form you and convert them to radians.
# then it will calculate and give you the cartesian coordinates.
import math# imports the math functions

x = float(input("What is the magnitude for x: "))# gets the information form you.
y = float(input("What is the magnitude for y: "))
d = float(input("What is the angle: "))
a = math.radians(d)# conversts to radians
def cosine():# function for the x coordinate
    x1= x * math.cos(a)
    print("x coordinate =", x1)
def sine():# function for the y coordinate
    y1= y* math.sin(a)
    print("y coordinate =", y1)

cosine()# call the function
sine()
