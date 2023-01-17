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
csvpath = os.path.join("Resouces", "pypoll_election_data.csv")
tot_votes = 0
candidate_names = []
candidate_names_and_votes_dict = {}
summary_of_candidates = ""
winner_name = []


