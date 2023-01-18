#   PyPoll:

#       Assignment Instructions:
#           Create a Python script that analyzes the votes of a small, rural town.

#           Analyze the votes and calculate each of the following values:
#               - The total number of votes cast 
#               - A complete list of candidates who received votes
#               - The percentage of votes that each candidate won
#               - The total number of votes that each candidate won
#               - The winner of the election based on popular vote

#               /////

#   Import all the required modules
import csv
import os

#   Assign location of csv which will be accessed
csvpath = os.path.join("Resources",  "election_data.csv")

#   Open the data for election results and read the csv file
with open(csvpath) as csvfile:
    data_set = csv.reader(csvfile, delimiter=",")

#   Initialize a total vote counter (set it to -1 to disregard the header row)
tot_votes = -1

#   Initialize counters for each candidate
Khan_count = Correy_count = Li_count = Otooley_count = 0

#   Initialize percentages for each candidaate's vote count
Khan_percent = Correy_percent = Li_percent = Otooley_percent = 0

#   Loop through all the rows of the data set
for row in data_set:

    #   Set up a counter that will account for the total number of rows
    #   to use for calculating the percentage of votes
    tot_votes += 1

#   Set up the conddtionals to identify contents of each 3rd column (county)
    if row[2] == "Khan":
        Khan_count += 1
    elif row[2] == "Correy":
        Correy_count += 1
    elif row[2] == "Li":
        Li_count += 1
    elif row[2] == "0'Toooley":
        Otooley_count += 1

    #   Loop through the dictionary to get the candidate name as a key and votes for the value
        #   Then create a dictionary that assigns each key to the respective candidate
        #   Include the amount of votes that they collected
        Results = {"Khan":Khan_count, "Correy":Correy_count, "Li":Li_count, "O'Tooley":Otooley_count}

#   Calculate the percentages of votes per candidate
    Khan_percent = (Khan_count / tot_votes) * 100
    Correy_percent = (Correy_count / tot_votes) * 100
    Li_percent = (Li_count / tot_votes) * 100
    Otooley_percent = (Otooley_count / tot_votes) * 100

#   Find the maximum value from the values within the ditionary and return its key, then store it as the 'Winner'
    Winner = max(Results, key=Results.get)
    toprint = f"""Election Results
---------------------------------
Total Votes: {tot_votes}
---------------------------------
Khan: {Khan_percent}% ({Khan_count})
Correy: {Correy_percent}% ({Correy_count})
Li: {Li_percent}% ({Li_count})
O'Tooley: {Otooley_percent}% ({Otooley_count})
---------------------------------
Winner: {Winner}
---------------------------------"""

#   Print it to the terminal
print(toprint)

#   Create a text file, print all over to the text file and close it
file = open("output.txt", "w")
file.write(toprint)
