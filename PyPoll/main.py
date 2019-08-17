#PyPoll

#Import & access data
import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')

#Define the variables--make names a list to loop all names from the 'Candidate' column & candidates' names ==0 to count their votes, 
total_votes = 0
Khan = 0
Correy = 0
Li = 0
OTooley = 0
names = [0]
khan = [1]
correy = [2]
li = [3]
otooley = [4]


#Open file and start loop
with open(election_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    for row in csvreader:
        #Count all votes
        total_votes = total_votes + 1
        names.append(row[0])

        #Count the votes of each candidate in the poll
        Khan = Khan + 1
        khan.append(names)

        Correy = Correy + 1
        correy.append(names)

        Li = Li + 1
        li.append(names)

        OTooley = OTooley + 1
        otooley.append(names)

        #Determine the winner from candidate vote count
        #If a candidate vote is greater than their competitors, they are the winner
        #Or function speeds up the process
        if Khan > Correy or Li or OTooley:
            Winner = "Khan"
        elif Correy > Li or OTooley or Khan:
            Winner = "Correy"
        elif Li > OTooley or Khan or Correy:
            Winner = "Li"
        else:
            Winner = "O'Tooley"
    
#Use basic functions to calculate the precentage of votes per candidate

   
    k_per = round(f"{khan}/ {total_votes}")
    c_per = round(f"{correy}/ {total_votes}")
    l_per = round(f"{li}/ {total_votes}")
    o_per = round(f"{otooley}/ {total_votes}")

#Create results table

#Print election results table
print('Election Results')
print('-------------------------')
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {k_per}% ({khan})")
print(f"Correy: {c_per}% ({correy})")
print(f"Li: {l_per}% ({li})")
print(f"O'Tooley: {o_per}% ({otooley})")
print('-------------------------')
print(f"Winner: {Winner}")
print('-------------------------')

# Export data to a text file
output_file = os.path.join("PyPoll_Results.txt")
with open(output_file, "w", newline="") as text:
    text.write('Election Resuls')
    text.write('-------------------------')
    text.write(f"Total Votes: {total_votes}")
    text.write('-------------------------')
    text.write(f"Khan: {k_per}% ({khan})")
    text.write(f"Correy: {c_per}% ({correy})")
    text.write(f"Li: {l_per}% ({li})")
    text.write(f"O'Tooley: {o_per}% ({otooley})")
    text.write('-------------------------')
    text.write(f"Winner: {Winner}")
    text.write('-------------------------')

#Sources:
# Python Reference Guide
# Python Cheat Sheet (www.datacamp.com)
# WWE Data activity
