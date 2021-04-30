#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 08:35:33 2021

@author: tjwilli
"""

import numpy as np
import matplotlib.pyplot as plt

def find_dt(vi,theta,g,y0,A,r0,C,m):
    """
    A function to find an appropriate time-step dt
    so that dv/dt changes little over the interval
    """
    #t1 is the "gravitational" timescale, the time it takes
    # for gravity alone to bring vi to 0
    t1 = vi / g
    t2 = np.sqrt(m/(2*C*A*r0*g))
    t3 = np.sqrt(m/(2*C*r0*vi))
    t4 = y0 / vi
    t0 = min([t1,t2,t3,t4])
    dt = 0.01 * t0
    print("Setting timestep: dt = {:.2E}".format(dt))
    return dt


def dvxdt(vx,vy,y,y0,A,r0,C,m):
    return -1/(2*m) * C*A*r0*np.exp(-y/y0)*vx*np.hypot(vx,vy)
def dvydt(vx,vy,y,y0,g,A,r0,C,m):
    return -g - 1/(2*m) * C*A*r0*np.exp(-y/y0)*vy*np.hypot(vx,vy)    

def solve(vi,theta,g,y0,A,r0,C,m):
    vx = [vi * np.cos(theta)]
    vy = [vi * np.sin(theta)]
    x = [0]
    y = [0]
    t = [0]
    dt = 0.01
    dt = find_dt(vi,theta,g,y0,A,r0,C,m)
    while y[-1] >= 0:
        vxprime = dvxdt(vx[-1],vy[-1],y[-1],y0,A,r0,C,m)
        vyprime = dvydt(vx[-1],vy[-1],y[-1],y0,g,A,r0,C,m)
        vx.append(vx[-1] + vxprime * dt)
        vy.append(vy[-1] + vyprime * dt)
        x.append(x[-1] + vx[-1] * dt)
        y.append(y[-1] + vy[-1] * dt)
        t.append(t[-1] + dt)
    return map(np.array,[x,y,t])
        
def read_config(fname):
    infile = open(fname)
    lines = infile.readlines()
    infile.close()
    opts = {}
    for line in lines:
        if line.startswith('#'):
            continue
        splt = line.split(':')
        if len(splt) != 2:
            continue
        key,val = splt
        key = key.strip()
        val = float(val)
        opts[key] = val
    return opts

def main():
    opts = read_config('config.txt')
    theta = float(input("Launch angle [deg]? "))
    vi = float(input("Initial speed [m/s]?" ))
    x,y,t = solve(vi,np.deg2rad(theta),opts['GRAV_ACCEL'],opts['SCALE_HT'],opts['AREA'],opts['DENSITY'],opts['DRAG_COEFF'],opts['MASS'])
    plt.plot(x,y)
    plt.xlabel('X [m]')
    plt.ylabel('Y [m]')
    xofymax = x[y.argmax()]
    ymax = y.max()
    plt.text(xofymax,ymax,r'$y_{{max}}$={:.1f} m'.format(ymax),ha='center',va='bottom')
    plt.text(x.max(),0,r'$x_{{max}}$={:.1f} m'.format(x.max()),ha='right',va='bottom')
    plt.axhline(0,c='gray')
    plt.text(x.max()/2,0,r'time of flight:{:.1f} s'.format(t.max()),ha='center',va='bottom')
    #plt.gca().set_aspect('equal')
    plt.show()
main()
