import csv
import os

#input and output files
file_to_load = os.path.join("Resources" , "election_data.csv")
file_to_output = os.path.join("Analysis" , "Results.txt")

#candidates and votes information
candidate_list = []
candidate_vote_count = {}
total_vote_count = 0
winning_total_count = 0
winning_candidate = ""

#retrieving information from csv file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)
    for row in reader:
        print(". ", end=""),
        total_vote_count = total_vote_count + 1

        candidate_name = row[2]

        #looping throught candidates
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_vote_count[candidate_name] = 0
            candidate_vote_count[candidate_name] = candidate_vote_count[candidate_name] + 1
with open(file_to_output, "w") as txt_file:

#showing the results
    election_results = (
        f"\n\Election Results\n"
        f"======================================================================\n"
        f"Total Votes: {total_vote_count}\n"
        f"======================================================================\n")

    print(election_results, end="")   
    txt_file.write(election_results) 
    
    #vote counting and percentage
    for candidate in candidate_vote_count:
        votes = candidate_vote_count.get(candidate)
        percentage = float(votes) / float(total_vote_count) * 100

        if (votes > winning_total_count):
            winning_total_count = votes
            winning_candidate = candidate
            vote_count = f"{candidate}: {percentage:.3f}% ({votes})\n"
            print(vote_count, end="")
            txt_file.write(vote_count)

    winning_candidate_results = (
        f"========================================================================\n"
        f"Winner: {winning_candidate}\n"
        f"=========================================================================\n")
    print(winning_candidate_results)
    txt_file.write(winning_candidate_results)






