miles = float(input("Enter the car’s mileage"))
age = float(input("Enter the car’s age"))
mpg = float(input("Enter the car’s fuel efficiency (miles per gallon)"))
price = float(input("Enter the price of the car"))
buyCar = False
if price > 30000:
    buyCar = False
else:
    if price > 20000:
        if miles < 15000 and age < 5:
            buyCar = True
        elif mpg > 45 and age < 5:
            buyCar = True
    elif price >10000:
        if miles < 30000 and age < 8:
            buyCar = True
    else:
        if miles < 50000 and age < 10:
            if mpg > 25:
                buyCar = True
