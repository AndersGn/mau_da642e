# Lab2: This Python script solves the problems outlined in assignment Task A2.3 V: Digital Health IoT dataset

# Download this dataset with sample of participants using an Apple Watch and a "FitBit"
# https://www.kaggle.com/datasets/aleespinosa/apple-watch-and-fitbit-data 
# there are three files inside archive. Download and extract "aw_fb_data" in the same folder as this file

# This script is used for:
# Spliting the dataset into three categories with the following distribution: Train (70%), Validation (15%), and Test (15%) 

# To use this script you need to install these libraries: pip install pandas scikit-learn

# Author: Anders Grahn
# Date: 2024-02-10

import pandas as pd # To import and analyze the Health IoT dataset
from sklearn.model_selection import train_test_split # Tools for predictive data analysis
import os # Use this to figure out our current folder

current_directory = os.getcwd() # This figures out the current folder
CSV_PATH = current_directory # Path for the CSV file to import

# Import the health data from the CSV file
physical_activity_df = pd.read_csv("{CSVPATH}/aw_fb_data.csv".format(CSVPATH=CSV_PATH))

# Split into train 70% and test 30%
X_train, X_test = train_test_split(physical_activity_df, test_size=0.3) # Split full dataset 100% into a 70% Training - 30% Test split

# Split into test 15% and validation 15%
X_test, X_validation = train_test_split(X_test, test_size=0.5) # Split the test 30% dataset with 50% to a 15% Test - 15% Validation split 