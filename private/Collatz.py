number = int(input("Enter an integer: "))

def collatz(number):
    if number % 2 == 0:
        number = number//2
        return number
    else:
        number = number * 3 + 1
        return number


while number != 1:
    print(number)
    number = collatz(number)
print(number)   
    
