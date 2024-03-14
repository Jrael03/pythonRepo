import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt

# THIS IS FOR SET 2. #

# This will read the external dataset that we have in excel.
df = pd.read_excel('/Users/jordanrael/Documents/pythonProjects/statsProject/statsStuff.xlsx', sheet_name='macEntries')

# Data verification
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print("\n")
print(df)
print("\n")
columnData = df['Time Interval Seconds'].tolist()

# This is for calculating the mean
meanVal = round(statistics.mean(columnData),2)
print(f"Mean of data set 2 is: {meanVal}")

# This is for calculating standard deviation
standDev = round(statistics.stdev(columnData),2)
print(f"Standard deviation of data set 2 is: {standDev}")

# Calculations for Q1, Q2, and Q3
quartileOne = np.percentile(columnData, 25)
quartileTwo = np.percentile(columnData, 50)
quartileThree = np.percentile(columnData, 75)
print(f"Q1 (25th percentile) = {round(quartileOne, 2)}, Q2 (50th percentile) = {round(quartileTwo, 2)}, Q3 (75th percentile)= {round(quartileThree,3)}")

# Calculates the range
range = max(columnData) - min(columnData)
print(f"Max value of set 2: {max(columnData)}")
print(f"Min value of set 2: {min(columnData)}")
print(f"Range for data set 2 is: {range}")

# Frequency Table
ranges = [(0, 20), (20, 40), (40, 60), (60, 80), (80, 100), (100, 120), (120, 140), (140, 160), (160, 180), (180, 200), (200, 220)]
counts = [0] * len(ranges)

for val in columnData:
    for i, (start, end) in enumerate(ranges):
        if start <= val <= end:
            counts[i] += 1
            break
for i, (start, end) in enumerate(ranges):
    print(f"{start}-{end}: {counts[i]}")

# Box-and-whisker plot
plt.title("Box plot")
plt.boxplot(columnData)
plt.show()

# Frequency Histogram
plt.title("Histogram")
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency")
plt.hist(columnData, bins=10)
plt.show()


