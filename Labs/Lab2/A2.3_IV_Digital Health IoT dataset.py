# Lab2: This Python script solves the problems outlined in assignment Task A2.3 IV: Digital Health IoT dataset

# Download this dataset with sample of participants using an Apple Watch and a "FitBit"
# https://www.kaggle.com/datasets/aleespinosa/apple-watch-and-fitbit-data 
# there are three files inside archive. Download and extract "aw_fb_data" in the same folder as this file

# This script is used for:
# Normalize the "age", "height", and "weight", and Standardize "steps" and "heart rate" columns in a separate column at the end of the dataframe

# To use this script you need to install these libraries: pip install pandas matplotlib

# Author: Anders Grahn
# Date: 2024-02-10

import pandas as pd # To import and analyze the Health IoT dataset
import matplotlib.pyplot as plt # To show the log transformation 
import os # Use this to figure out our current folder

current_directory = os.getcwd() # This figures out the current folder
CSV_PATH = current_directory # Path for the CSV file to import

# Import the health data from the CSV file
physical_activity_df = pd.read_csv("{CSVPATH}/aw_fb_data.csv".format(CSVPATH=CSV_PATH))

# Apply normalization technique and put in seperate columns at the end of the dataframe
physical_activity_df['age_normalized'] = (physical_activity_df['age'] - physical_activity_df['age'].min())/(physical_activity_df['age'].max() - physical_activity_df['age'].min())
physical_activity_df['height_normalized'] = (physical_activity_df['height'] - physical_activity_df['height'].min())/(physical_activity_df['height'].max() - physical_activity_df['height'].min())
physical_activity_df['weight_normalized'] = (physical_activity_df['weight'] - physical_activity_df['weight'].min())/(physical_activity_df['weight'].max() - physical_activity_df['weight'].min())

# Apply standardize technique and put in seperate columns at the end of the dataframe
physical_activity_df['steps_standardized']=(physical_activity_df['steps']-physical_activity_df['steps'].mean())/physical_activity_df['steps'].std()
physical_activity_df['heart_rate_standardized']=(physical_activity_df['hear_rate']-physical_activity_df['hear_rate'].mean())/physical_activity_df['hear_rate'].std()