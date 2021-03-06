import matplotlib.pyplot as plt
import random
import math
import time

l = 2
w = 2
r = 0.5
N = int(input("How many points? "))
inside = 0
total = 0
plt.xlim(-w/2,w/2)
plt.ylim(-l/2,l/2)
circ = plt.Circle(xy=(0,0),radius=r,fill=False,color='blue')
plt.gca().add_artist(circ)
plt.gca().set_aspect('equal')

start = time.time()
avg = 0.05
for i in range(N):
    total += 1
    x = random.uniform(-w/2,w/2)
    y = random.uniform(-l/2,l/2)
    if x**2 + y**2 <= r**2:
        inside += 1
        plt.scatter(x,y,color='green')
    else:
        plt.scatter(x,y,color='red')
    title = "Ntotal={} Ninside={} frac={:.2f} area (est)={:.2f} area (true)={:.2f}".format(total,inside,inside/total,inside/total*l*w,math.pi*r**2)
    plt.title(title)
    pause = 10 / N - avg
    if pause <= 0:
        pause = 1e-20
    
    #print(pause)
    #if N > 200:
    #    pause = 10 / N**2
    plt.pause(pause)
    stop = time.time()
    avg = (stop - start) / (i+1)
stop = time.time()
print(stop-start)
plt.show()
