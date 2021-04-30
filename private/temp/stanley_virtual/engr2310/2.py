PI = 3.14

def calc_area(radius):
    result = PI * radius**2
    #return result
    print("The area is",result)

radius = float(input("Enter the radius: "))
calc_area(radius)
