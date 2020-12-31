import os
import csv
import numpy as np

candidate = []

# Create the csv variable for file
election_csv = os.path.join("Resources", "election_data.csv")
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:
        # pull candidate into it's own list
        candidate.append(row[2])

# Define the function and have it accept the 'wrestler_data' as its sole parameter
def print_percentages(election_data):

# For readability, it can help to assign your values to variables with descriptive names
    cname = []
    totalvotes = len(election_data)
    print(f"Total Votes:  {totalvotes}")
    cname = np.unique(election_data)
    for cand in cname:
        votes = election_data.count(str(cand))
        percent = round(int(votes) / int(totalvotes), 2)
        print(f"{cand} : {votes} {percent}")

# calculate the total number of votes cast
# print complete list of candidates who received votes
# The percentage of votes each candidate won
# calculate the total number of votes each candidate won
# calculate the winner of the election based on popular vote.
print_percentages(candidate)