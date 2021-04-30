#Example
#input
# 5 * 4 * 3 * 2 * 1

#result = 1
#result = result * 5 --> 5
#result = result * 4 --> 5*4=20
#result = result * 3 --> 20*3 = 5*4*3


result = 1
number = int( input("Enter the number") )
while number > 0:
    result = result * number
    number = number - 1 #number-=1
print(result)
