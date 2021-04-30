g = 9.8

def max_height(vi,theta):
    math.radians(theta)
    vy = vi * math.sin(theta)
    h = vy**2 / 2 / g
    return h

theta = 30 #launch angle, in degrees
vi = 10 #intl speed, m/s
