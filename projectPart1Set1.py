import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt

# THIS IS FOR SET 1. #

# This will read the external dataset that we have in excel.
df = pd.read_excel('/Users/jordanrael/Desktop/statsStuff.xlsx', sheet_name='stockPrices')

# Data verification
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print("\n")
print(df)
print("\n")
columnData = df['Price of Stock as of 3pm CT'].tolist()

# This is for calculating the mean
meanVal = round(statistics.mean(columnData),2)
print(f"Mean of data set 1 is: {meanVal}")

# This is for calculating standard deviation
standDev = round(statistics.stdev(columnData),2)
print(f"Standard deviation of data set 1 is: {standDev}")

# Calculations for Q1, Q2, and Q3
quartileOne = np.percentile(columnData, 25)
quartileTwo = np.percentile(columnData, 50)
quartileThree = np.percentile(columnData, 75)
print(f"Q1 (25th percentile) = {round(quartileOne, 2)}, Q2 (50th percentile) = {round(quartileTwo, 2)}, Q3 (75th percentile)= {round(quartileThree,3)}")

# Calculates the range
range = max(columnData) - min(columnData)
print(f"Max value of set 1: {max(columnData)}")
print(f"Min value of set 1: {min(columnData)}")
print(f"Range for data set 1 is: {range}")

# Frequency Table
ranges = [(0, 500), (500, 1000), (1000, 1500), (1500, 2000), (2000, 2500), (2500, 3000), (3000, 3500)]
counts = [0] * len(ranges)

for val in columnData:
    for i, (start, end) in enumerate(ranges):
        if start <= val <= end:
            counts[i] += 1
for i, (start, end) in enumerate(ranges):
    print(f"{start}-{end}: {counts[i]}")

# Box-and-whisker plot
plt.title("Box plot")
plt.boxplot(columnData)
plt.show()

# Frequency Histogram
plt.title("Histogram")
plt.xlabel("Price Range")
plt.ylabel("Frequency")
plt.hist(columnData, bins=8)
plt.show()


