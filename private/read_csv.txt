import matplotlib.pyplot as plt

fname = 'data.csv'
infile = open(fname)
data = infile.read()
infile.close()

lines = data.split('\n')

mass = []
accl = []
for line in lines[1:]:
    str_mass, str_accl = line.split(',')
    mass.append(float(str_mass))
    accl.append(float(str_accl))

plt.scatter(mass,accl)
plt.xlabel('mass')
plt.ylabel('accel')
plt.show()
