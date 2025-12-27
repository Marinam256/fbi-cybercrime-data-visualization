# Parsing CSV File Headers

from pathlib import Path
import csv

path = Path('data/fbi_hacking_state_totals.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Reading state totals into a list

states = []
totals = []

for row in reader:
    state = row[0]
    total = int(row[1])
    states.append(state)
    totals.append(total)

# Combining and sorting to get the top 5

state_totals = list(zip(states, totals))
state_totals.sort(key=lambda x: x[1], reverse=True)

top_5 = state_totals[:5]

top_states = [state for state, total in top_5]
top_totals = [total for state, total in top_5]

print(top_5)

# Plotting state totals

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.bar(top_states, top_totals, width = 0.6, color = '#1f77b4' )

for i, v in enumerate(top_totals):
    plt.text(i, v + 8, str(v), ha='center', fontsize=12)

plt.title('Top 5 States: Hacking & Computer Invasion (2020–2025)', fontsize = 16)
plt.xlabel('State', fontsize = 14)
plt.ylabel('Total Offenses', fontsize = 14)
plt.ticklabel_format(style='plain', axis='y')

plt.tight_layout()
plt.show()