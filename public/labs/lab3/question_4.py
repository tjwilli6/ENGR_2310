done = False
n = 0
m = 100
while not done and n != m:
    n = int(input())
    if n < 0:
        done = True
        print("n =", n)
