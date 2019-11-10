from mpl_toolkits.basemap import Basemap
#import numpy as np
import matplotlib.pyplot as plt

m = Basemap(projection='mill',
           llcrnrlat = 25,
           llcrnrlon = -130,
           urcrnrlat = 50,
           urcrnrlon = -60, 
           resolution='l')

m.drawcoastlines()
m.drawcountries()
m.drawstates()
#m.drawcounties()
#m.etopo()
#m.bluemarble()

xs = []
ys = []
NYClat, NYClon = 40.7127, -74.0059
xpt, ypt = m(NYClon, NYClat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'c*', markersize=25)

LAlat, LAlon = 34.05, -118.25
xpt, ypt = m(LAlon, LAlat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'r^', markersize=25)


m.plot(xs, ys)

# draw the title.
plt.title('Azimuthal Equidistant Projection')
plt.show()