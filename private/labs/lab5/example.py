def func(number):
    print(number**2 - 1)

while True:
    num = int(input("Enter a number: "))
    if num == 999:
        break
    func(num)
