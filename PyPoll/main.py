PyPoll:

        Assignment Instructions:
        Create a Python script that analyzes the votes of a small, rural town.

        Analyze the votes and calculate each of the following values:
        - The total number of votes cast 
        - A complete list of candidates who received votes
        - The percentage of votes that each candidate won
        - The total number of votes that each candidate won
        - The winner of the election based on popular vote

/////

#   Import all the required modules
import os
import csv
import operator


#   Set a path for the file 
csvpath = os.path.join("Resources", "pypoll_election_data.csv")
tot_votes = 0
candidate_names = []
candidate_names_and_votes_dict = {}
summary_of_candidates = ""
winner_name = []


    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)

        for candidate_data in csvreader"
        
        #   Find the total number of votes cast
        #       Add the total of all rows (disregard the header row)
        tot_votes += 1

        #   List out all the unique candidates
        #   Start a dictionary with said candidates (note: set values to zero)
        if candidate_data[2] not in candidate_names
            candidate_names.append(candidate_data[2])
            candidate_names_and_votes_dict[candidate_data[2]] = 0

        #   Add the total votes to the dictionary keys
        candidate_names_and_votes_dict[candidate_data[2]] += 1

    #   Create a loop to get the percent values and
    #   combine all the variables from the dictionary into the string to present in the output
    for the key, value in candidate_names_and_votes_dict.items():
        vote_percentage = ((value/tot_votes)*100)
        summary_of_candidates += f"{key}: {vote_percentage.3f}% ({value})\n"

    
    #   Output: printed in txt file within the analysis folder
    output = (
            f"Election Results\n"
            f"-----------------\n"
            f"Total votes: {tot_votes}\n"
            f"-----------------\n"
            f"Summary for each candidate: {summary_of_candidates}"
            f"------------------\n"
            f"the Winner (of the election): {winner_name}\n"
            f"------------------\n")

    #   Print out the results to the terminal
    print(output)

    #   Print out all the outputs in the txt file within the analysis folder
    with open("PyPoll/Analysis/output.txt", "w") as txt_file"
        txt_file.write(output)