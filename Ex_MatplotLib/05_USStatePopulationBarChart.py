import matplotlib.pyplot as plt
import numpy as np
import csv

states = []
population = []
bg_color = 'black'
fg_color = 'gray'
xtick_color = 'orange'
ytick_color = 'yellow'
xlbl_color = 'orange'
ylbl_color = 'yellow'

with open('c:/users/anand/Exercises/Exercises/Ex_MatplotLib/USPopulation.csv', 'r') as us_csv:
    rows = csv.reader(us_csv, delimiter=',')
    for row in rows:
        states.append(row[0].split(',')[0])
        population.append(int(row[0].split(',')[1]))
        pass


fig = plt.figure(facecolor=bg_color, edgecolor=fg_color)
ax1 = plt.subplot2grid((1, 1), (0, 0))

ax1.patch.set_facecolor(bg_color)
ax1.xaxis.set_tick_params(color=xtick_color, labelcolor=xlbl_color)
ax1.yaxis.set_tick_params(color=ytick_color, labelcolor=ylbl_color)

# Graph border box
for spine in ax1.spines.values():
    spine.set_color('red')

# Set label for x-axis and rotate
plt.xticks(np.arange(len(states)), states)
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(90)

#plt.yticks(np.arange(len(population)), population)
for label in ax1.yaxis.get_ticklabels():
    label.set_rotation(90)

ax1.grid(True, color=fg_color, linestyle='-', linewidth=.5)    
    
#plt.subplots_adjust(left=0.01, bottom=0.16, right=3, top=1, wspace=0.2, hspace=0)
plt.subplots_adjust(left=0, bottom=0, right=2, top=1, wspace=0.2, hspace=0.2)

plt.bar(states, population)
plt.show() 