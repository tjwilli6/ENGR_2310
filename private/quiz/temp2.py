def collatz(number):
    if number % 2:
        result = 3 * number + 1
    else:
        result = number / 2
    return result
        
number = 15
collatz()
print("The result is:",result)
