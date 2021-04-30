#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 06:25:26 2021

@author: tjwilli
"""

"""
Author: T Williamson
Date:   March 8 2021
projectile2.py: a program to find the angle for max horizontal 
    displacement given an initial velocity and plot the results
"""

import math
import matplotlib.pyplot as plt

#grav accel on surface of Earth
G = 9.81 #m/s2

def time_of_flight(theta,vi,yi):
    """
    Given launch angle "theta" [radians], initial velocity "vi"
    [m/s], and  initial height "yi" [m], calculate
    the time of flight for a launched projectile
    """
    vy = vi * math.sin(theta)
    tof = ( vy + math.sqrt(vy**2 + 2*G*yi) ) / G
    return tof


def xrange(theta,vi,yi):
    """
    Given launch angle "theta" [radians], initial velocity "vi"
    [m/s], and  initial height "yi" [m], calculate
    the final horizontal range
    """
    vx = vi * math.cos(theta)
    tof = time_of_flight(theta,vi,yi)
    return vx * tof


def find_max(vi,yi,theta_min=0,theta_max=90,dtheta=0.1):
    """
    Given initial velocity and height, find theta which maximizes xrange 
    (over the range [theta_min,theta_max] )
    """
    #Eventual max xrange, and corresponding theta
    #Start at invalid value so the first loop replaces them
    xmax = -9999
    theta_of_xmax = -9999
    
    theta_vals = []
    x_vals = []
    theta = theta_min 
    while theta <= theta_max:
        delta_x = xrange(math.radians(theta),vi,yi)
        #Keep collection of theta and x for later plotting
        theta_vals.append(theta)
        x_vals.append(delta_x)
        
        if delta_x > xmax:
            xmax = delta_x
            theta_of_xmax = theta
        theta += dtheta
    return theta_of_xmax, xmax, theta_vals, x_vals


def main():
    vi = float(input("What is the initial velocity [m/s]? "))
    yi = float(input("What is the initial height [m]? "))
    theta,xmax,tvals,xvals = find_max(vi,yi)
    print( "Horizontal displacement is maximized at an angle of",theta,"degrees",\
                "with a value of",xmax,"meters.")
      
    plt.plot(tvals,xvals)
    plt.xlabel("angle [deg]")
    plt.ylabel("range [m]")
    
    #Plot a dashed line at the maximum
    label = 'x_max = {:.1f} m \n@ theta = {:.1f} deg'.format(xmax,theta)
    plt.axvline(theta,ls='--',c='gray',label=label)
    plt.legend()
    plt.title('xrange vs theta (vi={},yi={})'.format(vi,yi))
    plt.show()
    
main()