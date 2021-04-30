import matplotlib.pyplot as plt

#x = [1,2,3,4,5]
#y = [1,4,9,16,25]

#plt.plot(x,y)
#plt.show()


days = ['Monday','Tuesday', "Wensday", 'Thursday', 'Friday']
revenue =[13000,10000,14000,8000,9000]
plt.bar(days,revenue)
plt.xlabel("Days of Week")
plt.ylabel("revenue")
plt.label("Weekly Earnings")
plt.show()
