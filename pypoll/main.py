import os
import csv

# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length
​
# create the csv variable for file
bank_csv = os.path.join("..", "Resources", "election_data.csv")
​
with open(bank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

     # Read the header row first (skip this part if there is no header)
	    csv_header = next(csv_file)
        print(f"Header: {csv_header}")

# Test your function with the following:
#print(average([1, 5, 9]))
#print(average(range(11)))

#precip = [float(row[PRECIP]) for row in incsv]

#avg_precip = sum(precip, 0.) / (1 and len(precip))  # prevent div-by-0
#max_precip = max(precip)

#print(
#   "Avg precip: {:0.3f} in/day, max precip: {:0.3f} in/day"
#   .format(avg_precip, max_precip)
#)
​
    # Read through each row of data after the header
    for row in csv_reader:
​       # calculate total profit/loss
        profitloss = [float(row[1])]
        totalpl = totalpl + profitloss
        maxvalue = max(maxvalue, profitloss)
        minvalue = min(minvalue,profitloss)
        # Convert row to float and compare to grams of fiber
        if maxvalue = profitloss:
            maxdate = row[0]
         elif minvalue = profitloss:
             mindate = row[0]   
# calculate the total number of votes cast
print(len(profitloss))
​# print complete list of candidates who received votes
print(sum(profitloss)
# The percentage of votes each candidate won
print(average(profitloss))
#calculate the total number of votes each candidate won

# calculate the winner of the election based on popular vote.
