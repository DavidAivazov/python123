import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('database.csv')

# Task 1: Data Manipulation
# 1.1 Split 'Date' into 'Year', 'Month', 'Day'
df[['Year', 'Month', 'Day']] = df['Date'].str.split('/', expand=True)

# 1.2 Handle missing values by filling with a placeholder
df.fillna('Unknown', inplace=True)

# Task 2: Categorize Numeric Data
# Categorize the 'Magnitude' into 'Low', 'Medium', 'High'
bins = [0, 5, 7, 10]
labels = ['Low', 'Medium', 'High']
df['Magnitude_Category'] = pd.cut(df['Magnitude'], bins=bins, labels=labels)

# Task 3: Data Reshaping
# 3.1 Use melt to transform the dataframe
melted_df = pd.melt(df, id_vars=['Date'], value_vars=['Magnitude', 'Depth'])

# 3.2 Use pivot_table to create a summary table
pivot_df = df.pivot_table(values='Magnitude', index='Year', columns='Magnitude_Category', aggfunc='count', fill_value=0)

# Task 4: Visualization
# 4.1 Line plot of Earthquakes per Year
plt.figure(figsize=(10, 6))
df['Year'] = df['Year'].astype(int)
yearly_counts = df['Year'].value_counts().sort_index()
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values)
plt.title('Number of Earthquakes per Year')
plt.xlabel('Year')
plt.ylabel('Number of Earthquakes')
plt.show()

# 4.2 Bar plot of Earthquakes by Magnitude Category
plt.figure(figsize=(10, 6))
sns.countplot(x='Magnitude_Category', data=df, palette='viridis')
plt.title('Earthquakes by Magnitude Category')
plt.xlabel('Magnitude Category')
plt.ylabel('Count')
plt.show()

# 4.3 Scatter plot of Magnitude vs Depth
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Depth', y='Magnitude', data=df)
plt.title('Scatter plot of Magnitude vs Depth')
plt.xlabel('Depth')
plt.ylabel('Magnitude')
plt.show()

# 4.4 Pie chart of Earthquake Magnitude Categories
plt.figure(figsize=(8, 8))
magnitude_counts = df['Magnitude_Category'].value_counts()
plt.pie(magnitude_counts, labels=magnitude_counts.index, autopct='%1.1f%%', colors=sns.color_palette('viridis', 3))
plt.title('Pie Chart of Earthquake Magnitude Categories')
plt.show()

# Task 5: Date Transformations
# 5.1 Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# 5.2 Resample data to get the number of earthquakes per month
monthly_counts = df.resample('M', on='Date').size()

# Plot monthly earthquake counts
plt.figure(figsize=(10, 6))
monthly_counts.plot()
plt.title('Monthly Earthquake Counts')
plt.xlabel('Month')
plt.ylabel('Number of Earthquakes')
plt.show()
