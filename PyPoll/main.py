#!/usr/bin/env python
# coding: utf-8

# In[1]:


#set input filepath
import os
import csv
poll_csv = os.path.join(".","Resources","election_data.csv")


# In[2]:


#initialize variables
votes = 0
candidate_num = 0
candidate_votes = 0
candidates = []
counties = []


# In[3]:


#return candidate dictionary or null from candidates list
def search(candidate, candidates):
    try:
        for element in candidates:
            if element['candidate'] == candidate:
                candidate_found = element
                break
        return candidate_found
    except:
        return None


# In[4]:


#read and analyze data
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        # Increment total votes
        votes += 1
        # Read row
        voter = int(row[0])
        county = str(row[1])
        candidate = str(row[2])
        # Build county list
        if county not in counties:
            counties.append(county)
        # Get existing candidate record
        find_candidate = search(candidate, candidates)
        # If there is no candidate record, add candidate to list, otherwise, increment votes for candidate
        if find_candidate == None:
            new_candidate = {"candidate":candidate,"votes":1}
            candidates.append(new_candidate)            
        else:
            new_votes = {"votes":int(find_candidate['votes'])+1}
            for person in candidates:
                if person['candidate']==candidate:
                    person.update(new_votes)


# In[5]:


def print_and_save(message, f):
    print(message)
    f.write(f"{message}\n")


# In[6]:


# Print and save results
filename = "PyPoll.txt"
with open(filename, 'w') as f:
    print_and_save("Election Results",f)
    print_and_save("-----------------------------",f)
    print_and_save(f"Total Votes: {votes}",f)
    print_and_save("-----------------------------",f)
    highest_votes = 0
    winner = ""
    for person in candidates:
        name = person['candidate']
        vote_count = person['votes']
        if vote_count>highest_votes:
            highest_votes = vote_count
            winner = name
        vote_percent = round(vote_count*100/votes,1)
        print_and_save(f"{name} {str(vote_percent)}% ({vote_count})",f )
    print_and_save("-----------------------------",f)
    print_and_save(f"Winner: {winner}",f)
    print_and_save("-----------------------------",f)

