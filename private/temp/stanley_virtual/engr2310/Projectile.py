# Cameron Stanley
# 3-3-2021
# The code will ask for the Projectiles initial speed and initial height and will calculate the angle for you.

import math
# This is the initial height that the user gives.
yi = float(input("Enter the intial height above above the landing point in meters: "))
# This is the initial velocity that the user gives.
vi = float(input("Enter the initial speed in: "))

# This is the function to calculate the time of flight for the projectile.
def time_of_flight(theta,vi,yi):
    # Converts the angle in degrees to radian.
    theta = math.radians(theta)
    t_flight = (((vi* math.sin(theta))+((((vi**2)*((math.sin(theta))**2))+(2 * 9.81 * yi))**(1/2)))/ 9.81)
    return t_flight

# This is the function to calculate the range of x.
def xrange(theta,vi,yi):
    theta = math.radians(theta)
    x = vi* math.cos(theta)* time_of_flight(theta,vi,yi)
    return x
  
def main():
    # These two are zero so that way later in the code it can remeber the numbers that are needed for the angle.
    x_max = 0
    theta = 0
    # This loop is here because to get the angle we need to find the angle between 0-90 that gives us the maximum x rangle that can exist for the problem.
    while theta < 90:
        theta = theta + .1
        # x is used so the code will remember the x value and evaluate it to see if it is the biggest x can be. 
        x = xrange(theta,vi,yi)

        # The two statments are used so that the code will only remeber the maximum x value and the time of flight that goes with it.
        if x > x_max:
            t_flight = time_of_flight(theta,vi,yi)
            x_max = x
            
        else:
            continue

    # This part caculates the angle using the maximum x and its time of flight.
    # Then converts the angle back to degrees.
    angle = math.acos(x_max/(vi*t_flight))
    angle = math.degrees(angle)
    print("The angle of the Projectile is", angle)

main()

