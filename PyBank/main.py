#Dependencies 
import csv
import os

#Files
file_input = os.path.join("Resources", "budget_data.csv") 
file_output = os.path.join("Analysis" , "budget_analysis.txt")

with open(file_input) as finance_data:
    reader = csv.reader(finance_data)

