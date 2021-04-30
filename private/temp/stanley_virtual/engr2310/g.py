# Cameron Stanley
# 2-12-2021
# This code askes the user for the mass of the planet and radius of the planet
# and prints out the gravitational acceleration.

mass = float(input("What is the planets mass? ")) # the inputs for the equation
radius = float(input("What is the planets radius? "))
G = 6.7e-11# same as (6.7 * 10^-11)
def equation(mass, radius, G): # is the function.
    print("g = ", (G * mass)/(radius**2))#what the code out puts and the equation.
    

equation(mass, radius, G)

