# Parsing CSV File Headers

from pathlib import Path
import csv

path = Path('data/fbi_hacking_crime_5yr.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Reading and Creating Offense Counts into a List

offense_counts = []
first_row = next(reader)

for value in first_row[1:]:
    offense_counts.append(int(value))
print(offense_counts)

# Reading and Creating Months into a list

months = header_row[1:]
print(months)

# Importing Plotting 

import pandas as pd
import matplotlib.pyplot as plt

# Aggregate monthly counts into yearly totals

df = pd.DataFrame({
    'month': months,
    'offense': offense_counts
})
df['year'] = df['month'].str.split('-').str[1]
yearly_offenses = df.groupby('year')['offense'].sum()

# Plotting yearly totals

plt.figure(figsize=(10,6))
plt.plot(yearly_offenses.index, yearly_offenses.values, marker = 'o', linewidth = 2, color = '#1f77b4' )
plt.title("Hacking & Computer Invasion Trends in the U.S.", fontsize = 16)
plt.xlabel("Year", fontsize = 14)
plt.ylabel("Total Offenses", fontsize = 14)
plt.ticklabel_format(style='plain', axis='y')
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
plt.grid(True)
plt.show()

