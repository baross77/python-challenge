import os 
import csv

total_vote_count = 0
candidates = ""
candidate_votes = {}
candidate_percentage = {}
winner_votes = 0
winner = ""


with open ("full_election_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

# Determine total number of votes cast and per candidate votes
    for row in csvreader:
        total_vote_count = total_vote_count + 1

        candidates = row[2]
        if candidates in candidate_votes:
            candidate_votes[candidates] =  candidate_votes[candidates] +1
        else:
            candidate_votes[candidates]= 1

# candidate percentages
    for top_person, vote_count in candidate_votes.items ():
        candidate_percentage[top_person] = '{0:0%}'.format(vote_count/total_vote_count)
        if vote_count > winner_votes:
                winner_votes = vote_count
                winner = top_person


# Total votes, Candidates who received, percentage of votes, # of votes, and winner

    print ("Election Results")
    print ("-------------------------")
    print (f"Total Votes: {total_vote_count}") 
    print ("-------------------------")
    print (f"({candidates}: {candidate_percentage }{candidate_votes})")
    print ("-------------------------")
    print (f"Winner: {winner}")

# Export to text
save_file = "PyPoll".strip(".csv") + "_Full_Voting_Results.txt"
csvpath = os.path.join(".", save_file)
with open (csvpath, "w") as text:
    text.write ("Election Results" +"\n")
    text.write ("-------------------------"  + "\n")
    text.write (f"Total Votes: {total_vote_count}"  + "\n") 
    text.write ("-------------------------")
    text.write (f"({candidates}: {candidate_percentage }{candidate_votes})"  + "\n")
    text.write ("-------------------------"  + "\n")
    text.write (f"Winner: {winner}"  + "\n")