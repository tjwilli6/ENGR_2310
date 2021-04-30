speed_limit = 35
speed = float(input("Enter your speed"))
if speed > speed_limit - 5 and speed < speed_limit + 5:
    print("Car is driving within the speed limit")
elif speed < speed_limit - 5:
    print("Car is driving too slowly!")
else:
    print("Car is speeding! Get them!")
