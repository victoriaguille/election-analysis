#The data we need to retrieve
#1. The Total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

#add our dependencies
import csv
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join('resources', 'election_results.csv')
#assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#candidate options
candidate_options = []

#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read the header row
    headers = next(file_reader)

    #print each row in the csv file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)


#print the candidate list
print(candidate_options)

#3. print the total votes
print(total_votes)



#using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    #write three counties to the file
    txt_file.write("Counties in the Election\n__________________________________\nArapahoe\nDenver\nJefferson")


#close the file
outfile.close()


#close the file
election_data.close()