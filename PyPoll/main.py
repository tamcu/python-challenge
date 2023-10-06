import csv
from dataclasses import fields
import os

csvpath = os.path.join ('.','data1','election_data.csv')

# Create lists to hold the data and variables
list_of_votes = []
total_votes = 0
candidates = {}

# Open and read csv
with open(csvpath, encoding= 'UTF-8') as my_file:
    csv_reader = csv.reader(my_file)

# Read the header row first 
    header = next(csv_reader)

# Read through each row of data after the header
    for row in csv_reader:
        # Iterate to add the votes of each candidate and add the total votes
        total_votes +=1
        if row[2] in candidates:
            candidates[row[2]] +=1
        else:
            candidates[row[2]] =1

percentage_candidates = {}
winner = 0
candidate_winner = " "

#Iterate to fins the winner and obtain the percentages of the votes
for key in candidates:
    n = (candidates[key]/total_votes) * 100
    if n > winner:
        candidate_winner = key
        winner = n
    percentage_candidates[key] = n

#Print the results 
print("Election Results")
print("----------------------------")
print(f'Total Votes: {print(total_votes)}')
print("----------------------------")
print(f'Charles Casper Stockham: %{(percentage_candidates["Charles Casper Stockham"])} ({candidates["Charles Casper Stockham"]})')
print(f'Diana DeGette: %{(percentage_candidates["Diana DeGette"])} ({candidates["Diana DeGette"]})')
print(f'Raymon Anthony Doane: %{(percentage_candidates["Raymon Anthony Doane"])} ({candidates["Raymon Anthony Doane"]})')
print("----------------------------")
print(f"Winner: {candidate_winner}")
print("----------------------------")

#Print the results and create txt file
csvpath = os.path.join ('.','data1','election.txt')
with open("election.txt", "w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write(f'Total Votes: {print(total_votes)}')
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f'Charles Casper Stockham: %{(percentage_candidates["Charles Casper Stockham"])} ({candidates["Charles Casper Stockham"]})')
    file.write("\n")
    file.write(f'Diana DeGette: %{(percentage_candidates["Diana DeGette"])} ({candidates["Diana DeGette"]})')
    file.write("\n")
    file.write(f'Raymon Anthony Doane: %{(percentage_candidates["Raymon Anthony Doane"])} ({candidates["Raymon Anthony Doane"]})')
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Winner: {candidate_winner}")
    file.write("\n")
    file.write("----------------------------")
