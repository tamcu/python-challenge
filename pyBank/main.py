import csv
import os

csvpath = os.path.join ('.','data1','budget_data.csv')

# Create listts to hold the data
list_of_data = []
list_of_months = []
profit = []

# Open and read csv
with open(csvpath, encoding= 'UTF-8') as my_file:
    csv_reader = csv.reader(my_file)

# Read the header row first 
    header = next(csv_reader)

# Read through each row of data after the header
    for row in csv_reader:
        list_of_months.append(row[0])
        list_of_data.append(int(row[1]))
        
   # Calcualte the total number of months included in the dataset
    total_months = len(list_of_months)

    for x in range(len(list_of_data)-1):

        profit.append(list_of_data[x+1]-list_of_data[x])

    # Calcualte the net total amount of "Profit/Losses" over the entire period
    total = sum(list_of_data)

# Obtain the increases and decreases of the profits by obtaining max value, then relate them to the months to obtain the date
    max_value = max(profit)
    min_value = min(profit)

    max_month = profit.index(max(profit))
    min_month = profit.index(min(profit))

# Calcualte the average change
    average = round(sum(profit)/len(profit),2)

#Print the results 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {list_of_months[max_month]} (${(str(max_value))})")
print(f"Greatest Decrease in Profits: {list_of_months[min_month]} (${(str(min_value))})")

#Print the results and create txt file
csvpath = os.path.join ('.','data1','budget_results.txt')
with open("example.txt", "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {total_months}")
    file.write("\n")
    file.write(f"Total: ${total}")
    file.write("\n")
    file.write(f"Average Change: ${average}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_month]} (${(str(max_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[min_month]} (${(str(min_value))})")
