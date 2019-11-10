import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()

def create_plots():
    xs = []
    ys = []
    
    for i in range(10):
        x = i
        y = random.randrange(10)
    
        xs.append(x)
        ys.append(y)
    
    return xs, ys

# Using subplots to show multiple plots
#ax1 = fig.add_subplot(221)
#ax2 = fig.add_subplot(222)
#ax3 = fig.add_subplot(212)


# Using Subplot to grid to show multiple plots
# syntax subplot2grid((rows, cols), location, rowspan, colspan)
plt.title('Title of all graphs')

ax1 = plt.subplot2grid((6,2), (0, 0), rowspan = 3, colspan = 1)
plt.ylabel('y1 Units')

ax2 = plt.subplot2grid((6,2), (0, 1), rowspan = 3, colspan = 1)
plt.ylabel('y2 Units')

ax3 = plt.subplot2grid((6,2), (3, 0), rowspan = 3, colspan = 2)
plt.ylabel('y3 Units')


# Plot the drawings
x, y = create_plots()
ax1.plot(x, y)

x, y = create_plots()
ax2.plot(x, y)

x, y = create_plots()
ax3.plot(x, y)

# Display
plt.show()