# Lab2: This Python script solves the problems outlined in assignment A2.1 II: Hey Nano! What's the Temp
# Visualize the data with a line graph with two axes: time & temperature

# This script is used for:
# Visualising the data (collected via Arduino Rp2040 IMU) from /content/out/Temperatures.csv file by
# createing a line graph with two axes: time & temperature with these criteria:
# 1. The color of the line should be orange
# 2. Add labels for each axes (Temperature (degrees Celsius), Time(seconds)),
# 3. Turn on the grids 
# 4. Add legend on the top right corner - temperature

# To use this script you need to install these libraries: pip install numpy pandas matplotlib 

# Author: Anders Grahn
# Date: 2024-02-03

import matplotlib.pyplot as plt # To visualize the data
import pandas as pd # To import and analyze the temperature data
import os # Use this to figure out our current folder

current_directory = os.getcwd() # This figures out the current folder
CSV_PATH = "{dir}/A2.1_HeyNano_WhatTheTemp/content/out".format(dir=current_directory) # Path for the CSV file to import

# Import the temperature data from the CSV file
temperatures_df = pd.read_csv("{CSVPATH}/Temperatures.csv".format(CSVPATH=CSV_PATH))

# Data for plotting
temp = temperatures_df['temp']
timestamp = temperatures_df['timestamp'] * 0.001 # Multiply * 0.001 to convert from milliseconds to seconds

print(timestamp)

fig, ax = plt.subplots()
ax.plot(timestamp, temp, color="orange", label='temperature') # Sets the plot line to orange and then adds a legend label
plt.legend()
ax.set_xlabel('Time(seconds)')
ax.set_ylabel('Temperature(degrees Celsius)')
ax.grid()
plt.show()