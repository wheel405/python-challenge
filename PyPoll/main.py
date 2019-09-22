#This is main.py in PyPoll.

#create a python script and analyze the following items:
# The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.
#---------------------------
#initial import
import os
import csv

#define reader path
csvpath = os.path.join('Resources/election_data.csv')

#define variables

total_votes = 0
percent_of_votes=0
candidates=[]
votes_per_candidate = {}
winner_votes= 0
winner=""

#open csvreader and skip the header from the first row
with open(csvpath) as election_file:
    csvreader = csv.reader(election_file)
    next(csvreader)

#create loop which appends all candidates to a list and counts their number of votes
    for row in csvreader:
        total_votes=total_votes+1
        candidate=row[2]
          
#if candidate is not already in the list, add them to the dictionary
        if row[2] in votes_per_candidate.keys():
            votes_per_candidate[row[2]] = votes_per_candidate[row[2]] + 1
        else:
            votes_per_candidate[row[2]] = 1 


# Total Number of votes
total_number_votes = []
for key, value in votes_per_candidate.items():
    candidates.append(key)
    total_number_votes.append(value)

# Percentage of votes
percent_of_votes =[]
for n in total_number_votes:
    percent_of_votes.append(round(n/total_votes * 100, 1))
 
# Finding the winner
clean_data = list(zip(candidates, total_number_votes, percent_of_votes))

winner_list = []
for name in clean_data:
    if max(total_number_votes) == name[1]:
        winner_list.append(name[0])

# Print all data
print ("Election results :")
print("Total Votes :" + str(total_votes)) 
print("----------------------------------------")
print("Candidates: " + str(candidates))  
print("----------------------------------------")
print("Percentage of votes: " + str(percent_of_votes))
print("----------------------------------------")
print("Total Number of Votes: " + str(total_number_votes))
print("----------------------------------------")

# Writng output files
PyPoll = open("output.txt","w+")
PyPoll.write("Election Results")  
PyPoll.write('\n' + "Total_votes" + str(total_votes)) 
PyPoll.write('\n' + str(candidates))
PyPoll.write('\n' + str(percent_of_votes))
PyPoll.write('\n' + str(total_number_votes)) 
PyPoll.write('\n' + "Winner:" + winner)    




        
