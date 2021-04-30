#Cameron Stanley
#3-12-2021
# This program just changes the list that we were given in lab 7 for Computational Problem Solving.
# It only changes the list in the way the instructor wanted it to change.

#a
planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
print(planets[3])
#b
ind = planets.index("Saturn")
print(ind,"is",planets[ind])
#c
planets.append("Minerva")
print(planets)
#d
planets[2] = "Terra"
print(planets)
#e
del planets[3]
print(planets)
#f
x = 0
while x < 7:
    print("Planet",x,"is",planets[x])
    x = x + 1
    
