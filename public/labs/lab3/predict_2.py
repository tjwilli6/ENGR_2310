number = 0
total_sum = 0

print("Starting the loop now!")

while not number==0:
    number = float(input("Enter a number: "))
    if number==0:
        break
    total_sum += number
print(total_sum)
