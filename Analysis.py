import pandas as pd
import os

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
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

# Adding Month Column

all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')
print(all_data.head())

