#Cameron Stanley
#2-26-2021
# this code solves 2^2 in three different ways and tells you which of the three ways are faster.
x = 2# the numbers
y = 2
z= 1
N = 10000
import math# imports the math functions
import time# imports the time function
def pow1(x,y):# the first way is the basic way x^y.
    z1 = x**y
def pow2(x,y):# uses the math function
    z2 = math.pow(x,y)
    return z2
def pow3(x,y,z):# uses a loop to find x^y
    while y > 0:
        z = x*z
        return z
        y = y-1
tstart = time.time()#starts the clock.
for i in range(N):# is the loop for the power.
    pow1(x,y)
tstop = time.time()# stops the clock
print("Time elapsed for pow1: ",(tstop-tstart)/N)#tells you the time that passed.

tstart = time.time()
for i in range(N):
    pow2(x,y)
tstop = time.time()
print("Time elapsed for pow2: ",(tstop-tstart)/N)
      
tstart = time.time()
for i in range(N):
    pow3(x,y,z)
tstop = time.time()
print("Time elapsed for pow3: ",(tstop-tstart)/N)

