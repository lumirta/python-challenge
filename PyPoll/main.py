import os
import csv

election_csv = os.path.join(".." "Resources", "election_data.csv")

total_votes= 0
candidate_receivedvotes = ()

candidate_votes = {}

winner_vote= ""
totalnumver_won = 0
percentage_won = 0

with open(election_csv) as election_data:
       file_reader = csv.reader(election_data)

headers = next(file_reader)

for row in file_reader:
       total_votes += 1

       candidate_name = row[2]
if candidate_name not in candidate_receivedvotes: 
       candidate_receivedvotes.append(candidate_name)
       candidate_votes[candidate_name] = 0

       candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes: 
        
        votes = candidate_votes[candidate_name]
    
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
      
        print(candidate_results)
      

if (votes > totalnumver_won) and (vote_percentage > percentage_won ): 
            
            winning_count = votes
            winning_percentage = vote_percentage
            
            winning_candidate = candidate_name

winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------\n")
print(winning_candidate_summary)

