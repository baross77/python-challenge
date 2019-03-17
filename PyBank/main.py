import os
import csv

month_count = 0
total_profit = 0
last_month_profit = 0
current_month_profit = 0
profit_change = 0
profit_changes = []
months = []


with open ("PyBank.csv", 'r', newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)    

# Monthly changes in Profit/Loss
    for row in csvreader:
        month_count = month_count + 1
        months.append(row[0])
        current_month_profit = int(row[0].split(',')[1])
        total_profit = total_profit + current_month_profit
        if month_count > 1:
                profit_change = current_month_profit - last_month_profit
                profit_changes.append(profit_change)
        last_month_profit = current_month_profit

# Results
    sum_profit_changes = sum(profit_changes)
    average_change = sum_profit_changes / (month_count-1)
    max_increase = max(profit_changes)
    max_decrease = min(profit_changes)
    max_increase_month_index= (profit_changes.index(max_increase) + 1)
    max_decrease_month_index= (profit_changes.index(max_decrease) + 1)
    max_increase_month = months[max_increase_month_index]
    max_decrease_month = months [max_decrease_month_index]

    print ("Financial Analysis")
    print ("--------------------------------")
    print (f"Total Months: {month_count}")
    print (f"Total: ${total_profit}")
    print (f"Average Change: ${average_change}")
    print (f"Greatest Increase in Profits:{(max_increase_month.split(',')[0])} (${max_increase})")
    print (f"Greatest Decrease in Profits:{(max_decrease_month.split(',')[0])} (${max_decrease})")

 # Export to text
save_file = "PyBank".strip(".csv") + "_FinancialAnalysisResults.txt"
csvpath = os.path.join(".", save_file)
with open (csvpath, "w") as text:
    text.write ("Financial Analysis" + "\n")
    text.write ("--------------------------------" + "\n")
    text.write (f"Total Months: {month_count}" + "\n")
    text.write (f"Total: ${total_profit}" + "\n")
    text.write (f"Average Change: ${average_change}" + "\n")
    text.write (f"Greatest Increase in Profits:{(max_increase_month.split(',')[0])} (${max_increase})" + "\n")
    text.write (f"Greatest Decrease in Profits:{(max_decrease_month.split(',')[0])} (${max_decrease})" + "\n")