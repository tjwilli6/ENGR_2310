F1 = float(input("What is the magnitude of the first force (in Newtons)? "))
theta1 = float(input("What is the angle of the first force (in deg)? "))
F2 = float(input("What is the magnitude of the second force (in Newtons)? "))
theta2 = float(input("What is the angle of the second force (in deg)? "))

#Convert to radians
pi = 3.1415926
theta1_rad = theta1 * pi / 180
theta2_rad = theta2 * pi / 180

#Now get sines and cosines
#Fx1 = F1 * cos(theta1_rad)
#Fx2 = F2 * cos(theta2_rad)
#Fx3 = Fx1 + Fx2
#Fy1 = F1 * sin(theta1_rad)
#Fy2 = F2 * sin(theta2_rad)
#Fy3 = Fy1 + Fy2


#Get cosine of theta1
cos_theta1 = 0
#num_of_terms = int(input("How many terms to calculate? "))
#x = float(input("Point to evaluate cosine? "))
num_of_terms = 20
x = theta1_rad

n = 0
exponent = 0
sign = -1
total = 0
while n < num_of_terms:
    #term = x**exponent / exponent!
    #exponent_fact = ?
    result = 1
    number = exponent
    while number > 0:
        result = result * number
        number = number - 1 #number-=1
    sign = -1 * sign
    term_value = sign * x**exponent / result
    total = total + term_value
    n = n + 1
    exponent = exponent + 2
    
cos_theta1 = total



#Now get cosine of theta2
num_of_terms = 20
x = theta2_rad

n = 0
exponent = 0
sign = -1
total = 0
while n < num_of_terms:
    #term = x**exponent / exponent!
    #exponent_fact = ?
    result = 1
    number = exponent
    while number > 0:
        result = result * number
        number = number - 1 #number-=1
    sign = -1 * sign
    term_value = sign * x**exponent / result
    total = total + term_value
    n = n + 1
    exponent = exponent + 2
    
cos_theta2 = total


#Now get sin(theta1)
#num_of_terms = int(input("How many terms to calculate? "))
#x = float(input("Point to evaluate sine? "))
num_of_terms = 20
x = theta1_rad
n = 0
exponent = 1
sign = -1
total = 0
while n < num_of_terms:
    #term = x**exponent / exponent!
    #exponent_fact = ?
    result = 1
    number = exponent
    while number > 0:
        result = result * number
        number = number - 1 #number-=1
    sign = -1 * sign
    term_value = sign * x**exponent / result
    total = total + term_value
    n = n + 1
    exponent = exponent + 2
    
sin_theta1 = total



num_of_terms = 20
x = theta2_rad
n = 0
exponent = 1
sign = -1
total = 0
while n < num_of_terms:
    #term = x**exponent / exponent!
    #exponent_fact = ?
    result = 1
    number = exponent
    while number > 0:
        result = result * number
        number = number - 1 #number-=1
    sign = -1 * sign
    term_value = sign * x**exponent / result
    total = total + term_value
    n = n + 1
    exponent = exponent + 2
    
sin_theta2 = total

####
#Ok, now we have all of our sines and cosines

Fx3 = F1 * cos_theta1 + F2 * cos_theta2
Fy3 = F2 * sin_theta1 + F2 * sin_theta2

print("Net force is: ",Fx3,Fy3)
