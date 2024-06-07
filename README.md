Explanation:
Data Manipulation:
Split the 'Date' column into 'Year', 'Month', and 'Day'.
Handle missing values by replacing them with 'Unknown'.

Categorize Numeric Data:
Categorize the 'Magnitude' column into 'Low', 'Medium', and 'High' using the cut() function.

Data Reshaping:
Use melt() to transform the dataframe from wide to long format.
Use pivot_table() to create a summary table showing the count of earthquakes per year for each magnitude category.

Visualization:
Create four different types of plots: a line plot, a bar plot, a scatter plot, and a pie chart.

Date Transformations:
Convert the 'Date' column to datetime format.
Resample the data to get the number of earthquakes per month and plot the results.
This code will help you perform the required data analysis and visualizations on the "Significant Earthquakes 1965-2016" dataset.
