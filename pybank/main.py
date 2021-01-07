import os
import csv
profitloss = 0
maxvalue = 0
minvalue = 0
totalpl = 0
pldata = []

# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    return sum(numbers) / length

# create the csv variable for file
bank_csv = os.path.join("Resources", "budget_data.csv")

# Specify the file to write to
output_path = os.path.join("Analysis", "analysis.txt")

with open(bank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    # Read through each row of data after the header
    for row in csv_reader:
        profitloss = float(row[1])
        pldata.append(profitloss)
        totalpl = totalpl + profitloss
        maxvalue = max(maxvalue, profitloss)
        minvalue = min(minvalue,profitloss)
        # Convert row to float and compare to grams of fiber
        if maxvalue == profitloss:
            maxdate = str(row[0])
        elif minvalue == profitloss:
            mindate = str(row[0]) 

print("Financial Analysis")
print("-----------------------------")
#calculate the total number of months included in the dataset
print(f"Total Months:  {len(pldata)}")

#calculate the net total amount of "Profit/Losses" over the entire period
print(f"Total:  {sum(pldata)}")
#calculate the average of the changes in "Profit/Losses" over the entire period
print(f"Average Change: {average(pldata)}")
#calculate the greatest increase in profits (date and amount) over the entire period
print(f"Greatest Increase in profits: {maxdate} {maxvalue}")
#calculate he greatest decrease in losses (date and amount) over the entire period
print(f"Greatest Decrease in profits: {mindate} {minvalue}")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as file_obj:

    file_obj.write("Financial Analysis\n")
    file_obj.write("-----------------------------\n")
    file_obj.write("Total Months:  ")
    file_obj.write(str(len(pldata)))
    file_obj.write("\n")
    file_obj.write("Total:  ")
    file_obj.write(str(sum(pldata)))
    file_obj.write("\n")
    file_obj.write("Average Change: ")
    file_obj.write(str(average(pldata)))
    file_obj.write("\n")
    file_obj.write("Greatest Increase in profits:  ")
    file_obj.write(str(maxdate))
    file_obj.write("  ")
    file_obj.write(str(maxvalue))
    file_obj.write("\n")
    file_obj.write("Greatest Decrease in profits:  ")
    file_obj.write(str(mindate))
    file_obj.write("  ")
    file_obj.write(str(minvalue))
    file_obj.write("\n")
    file_obj.close()