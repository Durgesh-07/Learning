# Import required library

import pandas as pd
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"
df = pd.read_csv(filename)
# Print first five rows of the dataframe

print(df.head())

xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx'
df = pd.read_excel(xlsx_path)
print(df.head())
# Access to the column Length

x = df[['Quantity']]
print(x)

# Get the column as a series

x = df['Product']
print(x)  # series object

# Get the column as a dataframe

x = df[['Quantity']]
print(type(x))

# Access to multiple columns

y = df[['Product','Category', 'Quantity']]
print(y)
# Access the value on the first row and the first column

print(df.iloc[0, 0])
# Access the value on the second row and the first column

print(df.iloc[1,0])

# Access the value on the first row and the third column

print(df.iloc[0,2])

# Access the value on the second row and the third column
print(df.iloc[1,2])
# Access the column using the name

print(df.loc[0, 'Product'])

# Access the column using the name

print(df.loc[1, 'Product'])

# Access the column using the name

print(df.loc[1, 'CustomerCity'])

# Access the column using the name

print(df.loc[1, 'CustomerCity'])

# Slicing the dataframe

print(df.iloc[0:2, 0:3])

# Slicing the dataframe using name

print(df.loc[0:2, 'OrderID':'Category'])

new_index=['a','b','c','d','e']


df_new=df
df_new.index=new_index
print(df_new.loc['a', 'CustomerCity'])
print(df_new.loc['a':'d', 'CustomerCity'])