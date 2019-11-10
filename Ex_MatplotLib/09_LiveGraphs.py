import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
# Use subplot of size 1 x 1 as first sub plot indicated by the last parameter '1'
ax1 = fig.add_subplot(1, 1, 1)

def animate(i):
    graph_data = open('example.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1: # to skip empty line
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs, ys)

# Animate graph fig, use the function animate at interval 1 sec
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()