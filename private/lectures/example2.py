import matplotlib.pyplot as plt
#Read the data
infile = open('data.txt','r')
lines = infile.readlines()
infile.close()

x = []
y = []
for line in lines:
    if line.startswith('#') or len(line)==0:
        continue
    xval,yval = line.split(' ')
    x.append( float(xval) )
    y.append( float(yval) )


total_area = 0
for i in range(len(x)-1):
    h = y[i]
    dx = x[i+1] - x[i]
    area = h*dx
    total_area += area
print(total_area)
