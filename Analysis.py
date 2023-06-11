import pandas as pd
import os
import matplotlib.pyplot as plt
import openpyxl
import numpy as np

df = pd.read_csv("./Sales_Data/Sales_April_2019.csv")


files = [file for file in os.listdir('./Sales_Data')]

all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv("./Sales_Data/" + file)
    all_months_data = pd.concat([all_months_data, df])

all_months_data.to_csv("all_data.csv", index = False)

all_data = pd.read_csv("all_data.csv")

# Clean up data
# Drop rows of NAN

nan_df = all_data[all_data.isna().any(axis = 1)]

all_data = all_data.dropna(how = 'all')

# Find 'Or' and delete it
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

# Convert columns to the correct type

all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered']) # Make int
all_data['Price Each'] = pd.to_numeric(all_data['Price Each']) # Make float

# Adding Month Column

all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')

# Add a sales column

all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

results = all_data.groupby('Month').sum()

months = range(1, 13)

# Sales in USD by Month

'''
plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month number')
plt.show()
'''

# What US City had the highest number of sales

# Add a city column

# Use .apply()

def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]

all_data['City'] = all_data['Purchase Address'].apply(lambda x: get_city(x) + ' (' + get_state(x) + ')')

results = all_data.groupby('City').sum()
#print(results)


cities = [city for city, df in all_data.groupby('City')]

plt.ticklabel_format(style = 'plain')
plt.bar(cities, results['Sales'])
plt.xticks(cities, rotation = 'vertical', size = 8)
plt.ylabel('Sales in USD ($)')
plt.xlabel('City name')
plt.tight_layout()
plt.show()
