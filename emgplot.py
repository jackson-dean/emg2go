#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mpld3
from datetime import datetime
from matplotlib.ticker import FuncFormatter

fig, ax = plt.subplots()

#x holds time values, y(n) holds data for respective channels
x, y1, y2, y3 = [], [], [], []

#import raw data into a file object
f = open('AB.txt', 'r');

#iterate over file and format raw string data to something matplotlib actually likes
for line in f:

	#split each row on white space
	row = line.split()

	#convert H:M:S.f formatted string to datetime object
	xvalue = datetime.strptime(row[0], '%H:%M:%S.%f')

	#build our plot array values
	x.append(xvalue)
	y1.append(row[1])
	y2.append(row[2])
	y3.append(row[3])

#close file handler
f.close()

#format x ticks to 0 indexed position values instead of arbitrary seconds
def fmtFunc(x, pos):
	if(not pos is None):
		return pos - 1

#alias our func formatter
xfmt = FuncFormatter(fmtFunc)

#plot raw data for channel 1
plt.subplot(3, 1, 1)
plt.plot(x, y1)

#set x format
plt.gca().xaxis.set_major_formatter(xfmt)

#Set axis labels
plt.ylabel('Voltage')
plt.xlabel('Seconds')

#plot raw data for channel 2
plt.subplot(3, 1, 2)
plt.plot(x, y2)

#set x format
plt.gca().xaxis.set_major_formatter(xfmt)

#Set axis labels
plt.ylabel('Voltage')
plt.xlabel('Seconds')

#plot raw data for channel 3
plt.subplot(3, 1, 3)
plt.plot(x, y3)

#set x format
plt.gca().xaxis.set_major_formatter(xfmt)

#Set axis labels
plt.ylabel('Voltage')
plt.xlabel('Seconds')

#write figure out as html+javascript
html = mpld3.fig_to_html(fig)
f = open('emg.html', 'w');
f.write(html);
f.close()

plt.grid(True)
plt.show()




