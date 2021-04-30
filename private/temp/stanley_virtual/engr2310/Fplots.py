
import matplotlib.pyplot as plt
n = int(input("How many term?" ))#this is the input that you put in
x2 = 1#numbers that start the fibonacci sequence
x1 = 0
a = 0
xaxis = []
yaxis = []
n= n - 1#to account for the number printing of the first term.
print(x1)# prints the first number of the fibonacci sequence
while n > 0: #this is the loop
    x = x2 + x1
    x2=x1#remebers two numbers before.
    x1=x#remebers the number before.
    a = 1 + a
    xaxis.append(a)
    yaxis.append(x)
    n = n - 1#makes it so the cobe will only put out the terms that you asked for.

plt.scatter(xaxis,yaxis)
plt.label("Fibonacci Graph")
plt.xlabel("Number of The Term")
plt.ylabel("Value of The Term")
plt.show()
