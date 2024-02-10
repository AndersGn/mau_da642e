# Lab2: This Python script solves the problems outlined in assignment Task A2.3 I: Digital Health IoT dataset

# Download this dataset with sample of participants using an Apple Watch and a "FitBit"
# https://www.kaggle.com/datasets/aleespinosa/apple-watch-and-fitbit-data 
# there are three files inside archive. Download and extract "aw_fb_data" in the same folder as this file

# This script is used for:
# Based on the instruction on the distribution transformation, transform the "calories" column to take the shape of a distribution close to normal distribution. 
# Experiment with different transforms (log, cube, etc.) to find the right one. (1pts - Mandatory)

# To use this script you need to install these libraries: pip install pandas datetime matplotlib

# Author: Anders Grahn
# Date: 2024-02-09

import pandas as pd # To import and analyze the Health IoT dataset
import matplotlib.pyplot as plt # To show the log transformation 
import numpy as np # Add logarithm function
import os # Use this to figure out our current folder


# On https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy, I implement this to avoid what is called chained indexing
pd.options.mode.copy_on_write = True

current_directory = os.getcwd() # This figures out the current folder
CSV_PATH = current_directory # Path for the CSV file to import

# Import the health data from the CSV file
physical_activity_df = pd.read_csv("{CSVPATH}/aw_fb_data.csv".format(CSVPATH=CSV_PATH))

# Read the dataset to work with
physical_activity_df = physical_activity_df.copy()

# These are the transfomrations I have looked at

fig, ax = plt.subplots()

#Data Value transform
ax.set_title('Current data distribution')
physical_activity_df['calories'].hist() #The function plots the distribution of the data in the "target" column
plt.show()

#Log transform
ax.set_title('Log transform')
physical_activity_df['log'] = physical_activity_df['calories'].transform(np.log10)
physical_activity_df['log'].hist()
plt.show()

# Cube transform
ax.set_title('Cube transform')
physical_activity_df['cube'] = physical_activity_df['calories'].transform(lambda x: np.power(x, 5))
physical_activity_df['cube'].hist()
plt.show()

# I have not found which transition is the "right one", is it possible to have a "right one"? If so how?, I'm totaly lost here.