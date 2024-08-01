import os
import pickle
# We've imported other needed scripts and defined aliases. Please keep using the same aliases for them in this project.
import config as cfg
import zid_project2_characteristics as cha
import zid_project2_portfolio as pf
import util
import pandas as pd
import os
import numpy as np
from datetime import datetime
import toolkit_config as tcfg
import zid_project2_etl as etl




# Define the folder containing the .pkl files
FOLDER_PATH = '/Users/gautamaneja/PycharmProjects/z5505823_event_study/project2'

# Initialize a dictionary to store the loaded data from each .pkl file
data_dict = {}

# Iterate over all files in the specified folder
for filename in os.listdir(FOLDER_PATH):
    if filename.endswith('.pkl'):
        filepath = os.path.join(FOLDER_PATH, filename)
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
            data_dict[filename] = data

# Now `data_dict` contains the data from all .pkl files
# You can process or use this data as needed
for filename, data in data_dict.items():
    print(f"Data from {filename}:")
    print(data)
    print()
