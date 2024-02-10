# Lab2: This Python script solves the problems outlined in assignment Task A2.3 III: Digital Health IoT dataset

# Download this dataset with sample of participants using an Apple Watch and a "FitBit"
# https://www.kaggle.com/datasets/aleespinosa/apple-watch-and-fitbit-data 
# there are three files inside archive. Download and extract "aw_fb_data" in the same folder as this file

# This script is used for:
# Visualize "steps", "heart_rate", and "calories" of the first three participants in three plots with subplots (stacked plot), 
# in a way that the steps of each three participants are depicted with different colored lines, the same for other two datasets. 
# The legends should be on the top corner of each plot (participant #1, participant #2, participant #3) 

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
participants_df = participants_df.drop_duplicates(subset=['weight', 'age'])
# Select the three first participants
participants_df = participants_df.head(3)

# The labels
names = ['participant #1', 'participant #2', 'participant#3']

# The values
values_steps = list(participants_df['steps'])
values_heart_rate = list(participants_df['hear_rate'])
values_calories = list(participants_df['calories'])

bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

fig, axs = plt.subplots(1, 3, figsize=(15, 3))

axs[0].bar(names, values_steps, color=bar_colors, label=names)
axs[0].set_title('Steps')

axs[1].bar(names, values_heart_rate, color=bar_colors, label=names)
axs[1].set_title('Heart Rate')

axs[2].bar(names, values_calories, color=bar_colors, label=names)
axs[2].set_title('Calories')

# Apply these setting on all of the plots
for ax in axs[0],axs[1],axs[2]:
    ax.legend(loc="upper right") # Position the legend

plt.show()