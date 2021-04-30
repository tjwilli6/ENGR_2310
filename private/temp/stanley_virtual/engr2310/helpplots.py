import matplotlib.pyplot as plt
import math
#x = [1,2,3,4,5]
#y = [1,4,9,16,25]

#plt.plot(x,y)
#plt.show()

#plt.scatter(x,y,color='green')
#plt.xlabel("X")
#plt.ylabel("Y")
#plt.show()


#days = ['Monday','Tuesday', "Wensday", 'Thursday', 'Friday']
#revenue =[13000,10000,14000,8000,9000]
#plt.bar(days,revenue)
#plt.xlabel("Days of Week")
#plt.ylabel("revenue")
#plt.label("Weekly Earnings")
#plt.show()

#ex
g=9.9
def y(t,vi,theta,yi=0):
    result = yi+vi * math.cos(theta)*t
    return result

def x(t,vi,theta,xi=0):
    result = xi + vi *math.cos(theta) *t
    return result

def vy(t,vi,theta):
    result =vi - g *t
    return result

theta = math.radians(30)
vi = 100
time = []
yvals = []
t = 0
while t < 10:
    time.append(t)
    xvals.append(x(t,vi,theta))
    yvals.append(y(t,vi,theta))
    t+=0.01

plt.plot(time,xvals,label='X(t)')
plt.plot(time,yvals,label='Y(t)')
plt.xlabel('time [s]')
plt.ylabel('Displacement [m]')
plt.show
