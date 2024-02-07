# Lab2: This Python script solves the problems outlined in assignment A2.2 I: Freaking Frigid!

# Download this dataset of collecting in/out temperature data over 5 months in (appx. 97000 data rows): 
# Temperature Readings : https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices and save it in the same folder as this file

# This script is used for:
# I- Visualize the indoor and outdoor temperature in one plot with different colors of your choice for the last week (strt from the top 02-12-2018 to 08-12-2018). (2 pts-Mandatory)

# To use this script you need to install these libraries: pip install pandas matplotlib datetime

# Author: Anders Grahn
# Date: 2024-02-06

import matplotlib.pyplot as plt # To visualize the data
import pandas as pd # To import and analyze the temperature data
import os # Use this to figure out our current folder
import datetime # Let us create date to look for

current_directory = os.getcwd() # This figures out the current folder
CSV_PATH = current_directory # Path for the CSV file to import

# Import the temperature data from the CSV file
temperatures_df = pd.read_csv("{CSVPATH}/IOT-temp.csv".format(CSVPATH=CSV_PATH))

# Convert the timestamp to datetime format
temperatures_df['noted_date'] = pd.to_datetime(temperatures_df['noted_date'], format='%d-%m-%Y %H:%M') #convert string to timestamp and apply the timestamp format to our dataframe

# Make sure all dates are sorted so we can start from 02-12-2018 to 08-12-2018
temperatures_sorted_df = temperatures_df.sort_values(by=['noted_date'])

# Set the date to start looking for entries
startEntry = datetime.datetime(2018, 12, 2)

# Filter all rows with column 'noted_date' that start from 02-12-2018, so we get the last week of temperatures
temperature_selected_dates_df = temperatures_sorted_df[(temperatures_sorted_df['noted_date'] >=startEntry)]

# Remove any duplicate temp readings (based on the noted_date), since I want to remove the "noise" this creates
temperature_selected_dates_df = temperature_selected_dates_df.drop_duplicates(subset="noted_date", keep=False,)

# Get the indoor temperatures
temperature_indoor_df = temperature_selected_dates_df[temperature_selected_dates_df['out/in'] == "In"]

# Get the outdoor temperatures
temperature_outdoor_df = temperature_selected_dates_df[temperature_selected_dates_df['out/in'] == "Out"]

fig, ax = plt.subplots()
ax.plot(temperature_indoor_df['noted_date'], temperature_indoor_df['temp'], color="orange", label='indoor temperature') # Sets the plot line to orange and then adds a legend label
ax.plot(temperature_outdoor_df['noted_date'], temperature_outdoor_df['temp'], color="green", label='outdoor temperature') # Sets the plot line to green and then adds a legend label
plt.legend()
ax.set_xlabel('Time(seconds)')
ax.set_ylabel('Temperature(degrees Celsius)')
ax.grid()
plt.show()