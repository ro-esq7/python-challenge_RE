#PyBank - FINAL DRAFT

#Import & access data
import os
import csv

budget_info = os.path.join('Resources', 'budget_data.csv')

#Define variables (make 'count' and 'avg_change' lists to make values mutable & the variables = 0 toprevent summing values as it loops)
total_months = 0
total_amount = 0
pre_val = 0
change_val = 0
amt_change = 0
count = []
avg_change = []

#Open file and start loop
with open(budget_info, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    for row in csvreader:
        
        total_months = total_months + 1
        count.append(row[0])

        pre_val = int(row[1])
        total_amount = total_amount + pre_val

        if total_months > 1:
            amt_change = pre_val - change_val
            avg_change.append(amt_change)
            change_val = pre_val

#Create summary table using basic functions to calculate the sum, average, and greatest increase/decrease of values
#Index the avg_change to print the greatest profit increase/ decrease with their corresponding dates
total_value = sum(avg_change)
average_change = total_value/ (total_months - 1)
profit_inc = max(avg_change)
profit_dec = min(avg_change)

inc_date = avg_change.index(profit_inc)
dec_date = avg_change.index(profit_dec)

inc_month = count[inc_date]
dec_month = count[dec_date]

#Print the summary table
print('Financial Analysis')
print('------------------------------')
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print("Average Change:","${0:.2f}".format(average_change))
print(f"Greatest Increase in Profits: {inc_month} (${profit_inc})")
print(f"Greatest Decrease in Profits: {dec_month} (${profit_dec})")

#Export to text file
output_file = os.path.join("PyBank_Analysis.txt")
with open(output_file, "w", newline="") as text:
    text.write('Financial Analysis')
    text.write('------------------------------')
    text.write(f"Total Months: {total_months}")
    text.write(f"Total: ${total_amount}")
    text.write("Average Change: ${0:.2f}".format(average_change))
    text.write(f"Greatest Increase in Profits: {inc_month} (${profit_inc})")
    text.write(f"Greatest Decrease in Profits: {dec_month} (${profit_dec})")


# #Sources:
#     #Udemy Zip class activity
#     #WWE Data class activity