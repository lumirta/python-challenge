import os
import csv

budget_csv = os.path.join("...", "Resources", "budget_data.csv")

profit = []
monthly_changes = []
date = []

count = 0
total_profit = 0
total_changeprof = 0
initial_profit = 0

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)