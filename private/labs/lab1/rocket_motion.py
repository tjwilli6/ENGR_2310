vx = 7500
vy = 1300
vz = -1000

mag = (vx**2 + vy**2 + vz**2)**0.5

vhat_x = vx / mag
vhat_y = vy / mag
vhat_z = vz / mag

print("The unit vector is <",vhat_x,",",vhat_y,",",vhat_z,">")
