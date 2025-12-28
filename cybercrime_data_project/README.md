# FBI CDE Cybercrime Visualization (Student Project)
Author: Marina M.

# Overview
My project analyzes hacking and computer invasion offenses in the United States from 2020 to 2025 utilizing FBI CDE
data(https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/home). I chose this particular focus as it aligns with my interest in cybersecurity, and I wanted to strengthen my Python skills through real-world datasets. 

The main goal of this project is to visualize national trends over the last five years and compare states with the highest number of offenses during this period. I achieved this by learning data cleaning, aggregation, and visualization in Python.

# Data Source
Source- https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/home

The data used in this project comes from the FBI CDE (Crime Data Explorer), which provides official crime statistics reported by law enforcement agencies across the United States. My chosen dataset includes monthly offense counts of hacking and computer invasion crimes from January 2020 to December 2025. *This project is for educational purpose only and does not represent official FBI analysis.*

# What This Project Shows
-	How have hacking and computer invasion offenses changed nationally over time?
From 2021-2024, there was a steady increase in reported offenses, with the peak being in 2024. There are lower totals in 2020 and 2025 due to external factors.
-	Which U.S. states report the highest number of these offenses?
Colorado, Texas, Washington, Virginia, and Michigan. This may be reflected due to higher population, reporting participation, or presence of cybersecurity/law enforcement reporting systems. 

# National Trend Line Graph
This graph shows the total number of hacking and computer invasion offenses yearly in the United States.
- X-axis: Year (2020–2025).
- Y-axis: Total number of offenses. 
- Each data point represents the sum of all aggregated monthly offense counts for the given year.

# Top 5 States Bar Graph
This graph compares the five U.S. states with the highest reported number of hacking and computer invasion offenses.
- X-axis: State.
- Y-axis: Total number of offenses.
- Each bar represents total offense counts for a single state from January 2020 to December 2025.

# Key Takeaways
Throughout this project, I learned how to:
- Read and parse CSV files using Python.
- Aggregate monthly data into yearly totals.
- Use pandas for data manipulation.
- Create accurate data visualizations with matplotlib.
- Interpret real-world data trends.

# Next Steps
Future work includes integrating APIs to automate data collection, allowing for expanded trend analysis across different time periods and crime types.

# Notes
- Offense counts for 2020 are lower due to the COVID-19 pandemic.
- Offense counts for 2025 are lower due to incomplete reporting, as the year was not fully completed at the time of data collection.
- All data compiled for this project was sourced directly from the FBI CDE’s website and downloaded/ transferred as CSV files.
- Due to the filtering options on the FBI CDE’s website, I manually transferred the offense counts of all US states to a CSV file. 


