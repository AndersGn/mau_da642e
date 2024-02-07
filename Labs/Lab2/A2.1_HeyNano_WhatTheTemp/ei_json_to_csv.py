# This Python script is for sub-exercise I: converting Edge Impulse JSON to CSV format in Task A2.1: Hey Nano! What's the Temp
# Sub-exercises I task: Collect the data in a CSV file and submit it with the rest of your results 

# In this assigment we are to include this code: https://gist.github.com/ShawnHymel/35e38ce42d790704bcf6b2511039d4dc
# and I adapted this to be run on my Windows machine as a py file, so it can convert an exported Edge Impulse JSON file to CSV file format.

# To use this script you have to install this library: pip install ujson

# Author: Anders Grahn
# Date: 2024-02-03

import ujson
import csv
import os
import os # Use this to figure out our current folder

### Settings
current_directory = os.getcwd() # This figures out the current folder

HOME_PATH = "{dir}".format(dir=current_directory)              # Location of the working directory
DATASET_PATH = "{dir}/dataset".format(dir=current_directory)   # Upload your JSON samples to this directory
OUT_PATH = "{dir}/content/out".format(dir=current_directory)   # Where output files go (will be recreated)

### Read JSON files

# Go through each file in the input directory
for filename in os.listdir(DATASET_PATH):

  # Read the JSON file
  header = ["timestamp"]
  with open(os.path.join(DATASET_PATH, filename), 'r') as json_file:

    # Load JSON
    data = ujson.load(json_file)

    # Parse the sample rate, header, and data
    sample_rate = data['payload']['interval_ms']
    for heading in data['payload']['sensors']:
      header.append(heading['name'])
    values = data['payload']['values']

    # Write header to CSV file
    out_filepath = os.path.join(OUT_PATH, os.path.splitext(filename)[0] + ".csv")
    # Anders: Added newline='' to avoid empty rows between values
    with open(out_filepath, 'w', newline='') as csv_file: 
      writer = csv.writer(csv_file)
      writer.writerow(header)

      # Prepend timestamp and write data rows to CSV file
      for t, line in enumerate(values):
        timestamp = t * sample_rate
        line.insert(0, timestamp)
        writer.writerow(line)