import pandas as pd
import os
import matplotlib.pyplot as plt
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

plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month number')
plt.show()

