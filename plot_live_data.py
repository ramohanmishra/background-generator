#!/usr/bin/env python

## Plotting live data


import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation  import FuncAnimation

def animate(i):
	data = pd.read_csv('data.csv')
	x = data['x_value']
	y1 = data['total_1']
	y2 = data['total_2']

	plt.cla()
	plt.plot(x,y1, label='channel 1')
	plt.plot(x,y2, label='channel 2')

	plt.legend(loc='upper left')
	plt.tight_layout()

	
ani = FuncAnimation(plt.gcf(), animate, interval=1000)		# gcf(): get current figure, interval is in millisecond, so interval = 1000 or 1 sec


# plt.plot(x_vals,y_vals)


plt.tight_layout()
plt.show()