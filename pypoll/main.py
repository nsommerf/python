import os
import csv
import numpy as np

candidate = []

# Create the csv variable for file
election_csv = os.path.join("Resources", "election_data.csv")

# Specify the file to write to
output_path = os.path.join("Analysis", "analysis.txt")

with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    # print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:
        # pull candidate into it's own list
        candidate.append(row[2])

def print_lines(file_obb):
    print("-----------------------------")
    file_obb.write("-----------------------------\n")

# Define the function and have it accept the 'wrestler_data' as its sole parameter
def print_percentages(election_data, file_obb):

# For readability, it can help to assign your values to variables with descriptive names 
    winpercent = 0
    wincand = ''
    cname = []
    cname = np.unique(election_data)
    for cand in cname:
        votes = election_data.count(str(cand))
        percent = round(int(votes)*100 / int(totalvotes), 2)
        if (percent > winpercent):
            wincand = str(cand)
            winpercent = percent
        print(f"{cand} : {votes} {percent}%")
        file_obb.write(str(cand))
        file_obb.write(":  ")
        file_obb.write(str(votes))
        file_obb.write("  ")
        file_obb.write(str(percent))
        file_obb.write("%\n")
    print_lines(file_obb)
    print(f"Winner:  {wincand}")
    file_obb.write("Winner: ")
    file_obb.write(str(wincand))
    file_obb.write("\n")

# calculate the total number of votes cast
# print complete list of candidates who received votes
# The percentage of votes each candidate won
# calculate the total number of votes each candidate won
# calculate the winner of the election based on popular vote.
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as file_obj:
    print("Election Analysis")
    file_obj.write("Election Analysis\n")
    print_lines(file_obj)
    totalvotes = len(candidate)
    print(f"Total Votes:  {totalvotes}")
    file_obj.write("Total Votes:  ")
    file_obj.write(str(totalvotes))
    file_obj.write("\n")
    print_lines(file_obj)
    print_percentages(candidate, file_obj)
    print_lines(file_obj)
    file_obj.close()