# Lab2: This Python script solves the problems outlined in assignment A2.1 III: Hey Nano! What's the Temp 
# With the functions mentioned in the instruction above, write a code to delete rows with normal room temperature. 

# This script is used for:
# Delete rows with normal room temperature. Delete the normal room temperature (24.3 for example) to compress the signal. 
# Visualize the data with the previous task A.2.1_II criteria in a line graph. 
# Pay attention that you might be needing to change an interval (for example 24.2 - 24.5)

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

# Remove the normal room temperatures (and no, 27C-28C is not my normal room temperature it is 19C-20C, the longer my Arduino is on, the hotter it gets)
# Have also waved my hand above the temp to cool it down lower than the "normal" room temperature ;-), that is wy I got values like 24
temperatures_compressed_df = temperatures_df.query('temp <27 or temp > 28') #  Filter all rows with column 'temp' has value lower than 27 or higher than 28

# Data for plotting
temp = temperatures_compressed_df['temp']
timestamp = temperatures_compressed_df['timestamp'] * 0.001 # Multiply * 0.001 to convert from milliseconds to seconds

fig, ax = plt.subplots()
ax.plot(timestamp, temp, color="orange", label='temperature') # Sets the plot line to orange and then adds a legend label
plt.legend()
ax.set_xlabel('Time(seconds)')
ax.set_ylabel('Temperature(degrees Celsius)')
ax.grid()
plt.show()