import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

company = ['Google', 'Amazon', 'Microsoft', 'Facebook']
revenue = [90, 136, 89, 27]
profit  = [45, 85, 49, 15]

xpos = np.arange(len(company))
ypos = np.arange(len(revenue))

plt.xticks = (xpos, company)
plt.yticks = (ypos, revenue)

plt.bar(xpos-0.1, revenue, width=0.2, label = 'Revenue')
plt.bar(xpos+0.1, profit,  width=0.2, label = 'Profit')

plt.xlabel(company)
plt.ylabel(revenue)
plt.title("US Tech Stocks")
plt.legend()