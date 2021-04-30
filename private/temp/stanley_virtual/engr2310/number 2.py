n = -1
c= 0
while c == 0:
    x = input("Enter number")
    n+=1
    y = x*(2**n)
    if x == 1:
        continue
    elif x == 0:
        continue
    else:
        print(y)
        break
        
