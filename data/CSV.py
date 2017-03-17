# -*- coding: UTF-8 -*-
import csv
import numpy as np
import pylab as pl
import glob
import matplotlib.pyplot as plt

a = []
files = glob.glob ("*.csv")
for file in files:
	with open(file) as f:
		reader = csv.reader(f)
		reader.next()
		for row in reader:
			if '1234.567g9' in row:
				try:
					a.pop()
				except IndexError:
					pass	
			else:	
				a.append(row[1])		

def plot():
	y = a
	N = len(y)
	x = range(N)
	width = 1.5
	plt.bar( x, y, width, color="blue")
	plt.show()

plot()	
