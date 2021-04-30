PI = 3.14

def calc_area(radius):
    result = PI * radius**2
    return result

r = float(input("Enter the radius: "))
calc_area(r)

print("The area is",result)
