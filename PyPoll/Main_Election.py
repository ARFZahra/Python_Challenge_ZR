import os
import csv

# Input and output path
vote_data_path = os.path.join(".", "Resources", "election_data.csv")


def analyze_election_data(vote_data):
    # Initialize variables
    total_votes = 0
    candidate_votes = {}

    # Read the CSV file
    with open(vote_data, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

         # Read the header row first
        csv_header = next(csvreader)
        
        # Count the votes for each candidate
        for row in csvreader:
            total_votes += 1
            candidate = row[2]
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1

    # Calculate percentages and find the winner 
    percentages = {}
    max_votes = 0
    winner = None
    for candidate, votes in candidate_votes.items():
        percentage = round((votes / total_votes) * 100, 3)
        percentages[candidate] = percentage
        if votes > max_votes:
            max_votes = votes
            winner = candidate


    return total_votes, percentages, winner, candidate_votes

# Call the function and print the result
total_votes, percentages, winner,candidate_votes = analyze_election_data(vote_data_path)


# Print the analysis

print("Election results")

print("----------------------------")

print(f"Total Votes: {total_votes}")

print("----------------------------")

for candidate, percentage in percentages.items():
    print(f"{candidate}: {percentage}% ({candidate_votes[candidate]})")
print("----------------------------")

print(f"Winner: {winner}")

print("----------------------------")


# Path to the output file
output_file_path = os.path.join(".", "Analysis", "election_results.txt")

# Write the results to the output file in new lines. 
with open(output_file_path, "w") as file:
    file.write(
        "Election results\n"
        "----------------------------\n"
        f"Total Votes: {total_votes}\n"
        "----------------------------\n")
    for candidate, vote_percentage in percentages.items():
        file.write(f"{candidate}: {vote_percentage:.3f}% ({candidate_votes[candidate]} votes)\n")
     
    file.write(
        "----------------------------\n"
        f"Winner: {winner}\n"
        "----------------------------\n")

    # (used Xpert learning assitant and chatgtp to understand and debugging codes). 
