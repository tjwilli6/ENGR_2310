num_of_terms = int(input("How many terms to calculate? "))
x = float(input("Point to evaluate sine? "))

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
    
print(total)
