F1 = float(input("What is mag of first force? "))
theta1 = float(input("What is the angle of first force"))
F2 = float(input("What is mag of second force? "))
theta1 = float(input("What is the angle of second force"))

#convert angles to radians
pi = 3.1415926535
theta1_rad = theta1 * pi / 180
theta2_rad = theta2 * pi / 180

#now get sines and cosine
#num_of_terms = int(input("How many terms to calculate? "))
#x = float(input("Point to evaluate sin? "))
num_of_terms = 20
x = theta1_rad
n = 0
exponent = 0
sign = -1
total = 0
while n < num_of_terms:
    #term = x**exponent / exponent
    #exponent_fact = ?
    result = 1
    number = exponent
    while number > 0:
        result = result * number
        number = number - 1
    sign = -1 * sign
    term_value = sign * x**exponent / result
    total = total + term_value
    n = n + 1
    exponent = exponent + 2
cos_theta1 = total
num_of_terms = 20
x = theta2_rad
n = 0
exponent = 0
sign = -1
total = 0
while n < num_of_terms:
    #term = x**exponent / exponent
    #exponent_fact = ?
    result = 1
    number = exponent
    while number > 0:
        result = result * number
        number = number - 1
    sign = -1 * sign
    term_value = sign * x**exponent / result
    total = total + term_value
    n = n + 1
    exponent = exponent + 2
cos_theta2 = total

num_of_terms = 20
x = theta1_rad
n = 0
exponent = 1
sign = -1
total = 0
while n < num_of_terms:
    #term = x**exponent / exponent
    #exponent_fact = ?
    result = 1
    number = exponent
    while number > 0:
        result = result * number
        number = number - 1
    sign = -1 * sign
    term_value = sign * x**exponent / result
    total = total + term_value
    n = n + 1
    exponent = exponent + 2
sin_theta1 = total
num_of_terms = 20
x = theta2_rad
n = 0
exponent = 0
sign = -1
total = 0
while n < num_of_terms:
    #term = x**exponent / exponent
    #exponent_fact = ?
    result = 1
    number = exponent
    while number > 0:
        result = result * number
        number = number - 1
    sign = -1 * sign
    term_value = sign * x**exponent / result
    total = total + term_value
    n = n + 1
    exponent = exponent + 2
sin_theta1 = total


Fx3 = F1 * cos_theta1 + F2 * cos_theta2
fy3 = F2 * sin_theta1 + F2 * sin_theta2

print("Net force is: ", Fx3,fy3)
