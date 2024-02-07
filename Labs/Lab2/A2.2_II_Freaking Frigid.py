# Lab2: This Python script solves the problems outlined in assignment A2.2 II: Freaking Frigid!

# Download this dataset of collecting in/out temperature data over 5 months in (appx. 97000 data rows): 
# Temperature Readings: https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices and save it in the same folder as this file

# This script is used for:
# II- Do these modifications on the dataframe made from the CSV dataset: (3pts Mandatory)

# Change the "In" and "Out" text of the "Out\In" column to 1 and 0 respectively.
# Separate the date and time in the "noted_date" column, into two separate columns.
# Keep only the data of the last day 08-12-2018, and remove the rest of the rows with the appropriate function
# Submit the modified CSV and your code together.

# To use this script you need to install these libraries: pip install pandas datetime
# The modified CSV file is saved as: temperatures_data.csv , in the same folder that this file is executed

# Author: Anders Grahn
# Date: 2024-02-07

import pandas as pd # To import and analyze the temperature data
import os # Use this to figure out our current folder
import datetime # Lets us create a date object to work with


# I got a warning "A value is trying to be set on a copy of a slice from a DataFrame.", when I was working with converting date back to string and found this:
# "We recommend turning Copy-on-Write on to leverage the improvements with pd.options.mode.copy_on_write = True` even before pandas 3.0 is available."
# On https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy, so I implement this and got rid of the "A value..." warning message.
pd.options.mode.copy_on_write = True

current_directory = os.getcwd() # This figures out the current folder
CSV_PATH = current_directory # Path for the CSV file to import

# Import the temperature data from the CSV file
temperatures_df = pd.read_csv("{CSVPATH}/IOT-temp.csv".format(CSVPATH=CSV_PATH))

# Change all the Out (outdoor) values to 1, I also make sure that we only look in the 'out/in' column
temperatures_df.replace(['out/in', "Out"], 1, inplace=True)

# Change all the In (indoor) values to 0, I also make sure that we only look in the 'out/in' column
temperatures_df.replace(['out/in', "In"], 0, inplace=True)

# Convert the 'noted_date' column to datetime format so we know what type we are working on
temperatures_df['noted_date'] = pd.to_datetime(temperatures_df['noted_date'], format='%d-%m-%Y %H:%M') 

# To seperate the 'noted_date' column into two new date and time columns, I got inspiration from here: https://stackoverflow.com/questions/65770998/converting-datetime-only-to-time-in-pandas
# "pandas has no separate datatypes for date and time. if you only want your columns to show date or time resp., you could format to string (strftime)"

# Separate the date in the "noted_date" column to a new column named date and save it as a string to make sure we only get at date
temperatures_df['date'] = temperatures_df['noted_date'].dt.strftime('%d-%m-%Y')

# Separate the time in the "noted_date" column to a new column named time and save it as a string to make sure we only get time
temperatures_df['time'] = temperatures_df['noted_date'].dt.strftime("%H:%M")

# Make sure all dates are sorted so we can start from 02-12-2018 to 08-12-2018
temperatures_sorted_df = temperatures_df.sort_values(by=['noted_date'])

# Set the date to start looking for entries
startEntry = datetime.datetime(2018, 12, 8)

# Filter all rows with column 'noted_date' that start from 08-12-2018, so we only get the last day of temperatures (removes the rest of the rows from our new dataset)
temperatures_selected_dates_df = temperatures_sorted_df[(temperatures_sorted_df['noted_date'] >=startEntry)]

# Remove any duplicate temp readings (based on the noted_date), since I do not want to save unessesary ("noisy") data
temperatures_selected_dates_df.drop_duplicates(subset="noted_date", keep=False)

# Now we are done working with the date format, so lets change it back into string as it where in the original CSV file
temperatures_selected_dates_df['noted_date'] = temperatures_selected_dates_df['noted_date'].dt.strftime('%d-%m-%Y %H:%M')

# Save the DataFrame to a CSV file (I wanted to, but I did not remove the 'noted_date' column, since this was not specified in this assigment)
temperatures_selected_dates_df.to_csv('temperatures_data.csv', index=False) 