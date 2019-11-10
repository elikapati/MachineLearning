import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
maxtemp = [50,52,39,48,20,80,45]
mintemp = [23,45,12,25,10,40,25]
avgtemp = [36,47,25,35,15,60,35]

plt.plot(x, maxtemp, marker='.', label="Max Temp", markersize=12, animated=1)
plt.plot(x, mintemp, marker='.', label="Min Temp", markersize=12, animated=1)
plt.plot(x, avgtemp, marker='.', label="Avg Temp", markersize=12, animated=1)
plt.xlabel('Day')
plt.ylabel('Temperature in C')
plt.title("Weather Report")
plt.legend(loc="best", shadow='true', fontsize='large')
plt.grid()
plt.show()
