import serial
import time
import matplotlib.pyplot as plt
import numpy as np
import csv

plotData = False

# open connection to arduino
ser = serial.Serial('/dev/cu.usbserial-AK061JAI', 9600)
ser.flushInput()

# data visualisation
if(plotData):
	plot_window = 20
	y_var = np.array(np.zeros([plot_window]))
	plt.ion()
	fig, ax = plt.subplots()
	line, = ax.plot(y_var)


# continuesly read serial input and write it to a csv file
with open("pressure_log.csv","a") as hLogfile:
	writer = csv.writer(hLogfile,delimiter=",")

	while True:
		readVal = float(ser.readline())
		writer.writerow([time.time(),readVal])
		print(str(time.time()) + ": " + str(float(ser.readline())))
		hLogfile.flush()
		if(plotData):
			y_var = np.append(y_var,readVal)
			y_var = y_var[1:plot_window+1]
			line.set_ydata(y_var)
			ax.relim()
			ax.autoscale_view()
			fig.canvas.draw()
			fig.canvas.flush_events()