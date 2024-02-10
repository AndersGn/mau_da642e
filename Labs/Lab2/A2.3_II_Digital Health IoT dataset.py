# Lab2: This Python script solves the problems outlined in assignment Task A2.3 II: Digital Health IoT dataset

# Download this dataset with sample of participants using an Apple Watch and a "FitBit"
# https://www.kaggle.com/datasets/aleespinosa/apple-watch-and-fitbit-data 
# there are three files inside archive. Download and extract "aw_fb_data" in the same folder as this file

# This script is used for:
# The data reflects 49 participants. Make a copy of the original dataframe and Find a way to keep one sample from each participant.  
# Therefore, the new dataframe should have 49 rows. You should use a specific function or a mix of functions in the instruction. 
# Afterward, visualize the "age", "height", and "weight" of the participants on each subplot (stacked plot). Grids should be on, 
# Legends should be on top, and The color of the line plot for each subplot should be different

# To use this script you need to install these libraries: pip install pandas matplotlib

# Author: Anders Grahn
# Date: 2024-02-09

import pandas as pd # To import and analyze the Health IoT dataset
import matplotlib.pyplot as plt # To show the log transformation 
import os # Use this to figure out our current folder

current_directory = os.getcwd() # This figures out the current folder
CSV_PATH = current_directory # Path for the CSV file to import

# Import the health data from the CSV file
physical_activity_df = pd.read_csv("{CSVPATH}/aw_fb_data.csv".format(CSVPATH=CSV_PATH))

# Make a copy of the original dataframe
participants_df = physical_activity_df.copy()

# Keep one sample from each participant (49 rows)
participants_df = participants_df.drop_duplicates(subset=['weight', 'height'])

# The number of participants to put on the x axis
x_number_of_participants = range(len(participants_df)) # Get a list that corresponds to the total number of participants

# Participant personal data
y_participant_age =  participants_df['age'].values # A list of the participants ages
y_participant_weight =  participants_df['weight'].values # A list of the participants weights
y_participant_height = participants_df['height'].values # A list of the participants hights

# Ceate a subplot for three plots
fig, axs = plt.subplots(3, sharex=True) # Share the x axis intervals
fig.suptitle('Participants') # Create a title

# Plot the Age
axs[0].plot(x_number_of_participants, y_participant_age, label="Age", color="orange")

# Plot the Weight
axs[1].plot(x_number_of_participants, y_participant_weight, label="Weight", color="green")

# Plot the Height
axs[2].plot(x_number_of_participants, y_participant_height, label="Height", color="red")

# Apply these setting on all of the plots
for ax in axs[0],axs[1],axs[2]:
    ax.grid(True) # Turn on Grid
    ax.legend(loc="upper center") # Position the legend

# Show the subplots
plt.show()