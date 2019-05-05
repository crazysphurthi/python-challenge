import os
import csv

budget_file = os.path.join("budget_data.csv")

# initialize variables
month = []
profit_loss = []
change_in_profit_loss = [0]

# read csv data
with open(budget_file, newline="") as file:
    budget_reader = csv.reader(file, delimiter=",")

    budget_header = next(budget_reader)
    #print(f"{budget_header}")

    for row in budget_reader:
        month.append(row[0])
        profit_loss.append(int(row[1]))
        #print(f"Month {row[0]}; Profit_Loss {row[1]}; Profit_Loss {type(row[1])}")

# total number of months
total_months = len(month)
#print(f"Total Months: {total_months}")

# Total amount of Profit/Lasses
total_profit_loss = 0
for i in profit_loss:
    total_profit_loss = total_profit_loss + i
#print("Total: " + "${0}".format(total_profit_loss))
#print("Total: " + "${:.2f}".format(total_profit_loss))

# Average of the changes in Profit/Losses over the entire period
total_change_in_profit_loss = 0
for i in range(1, total_months):
    change = profit_loss[i] - profit_loss[i-1]
    total_change_in_profit_loss = total_change_in_profit_loss + change
    change_in_profit_loss.append(change)

average_change_in_profit_loss =  total_change_in_profit_loss / (len(change_in_profit_loss) - 1)
#print("Average Change: " + "${:,.2f}".format(average_change_in_profit_loss))

# greatest increase in profits (date and amount)
max_position = change_in_profit_loss.index(max(change_in_profit_loss))
#print(f"Greatest Increase in Profits: {month[max_position]} (${change_in_profit_loss[max_position]})")

# greatest decrease in profits (date and amount)
min_position = change_in_profit_loss.index(min(change_in_profit_loss))
#print(f"Greatest Decrease in Profits: {month[min_position]} (${change_in_profit_loss[min_position]})")

# print Financial Analysis on Terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print("Total: " + "${0}".format(total_profit_loss))
print("Average Change: " + "${:,.2f}".format(average_change_in_profit_loss))
print(f"Greatest Increase in Profits: {month[max_position]} (${change_in_profit_loss[max_position]})")
print(f"Greatest Decrease in Profits: {month[min_position]} (${change_in_profit_loss[min_position]})")

# print Financial Analysis to a text file
str1 = "Total Months: {0}\n".format(total_months)
str2 = "Total: " + "${0}\n".format(total_profit_loss)
str3 = "Average Change: " + "${:,.2f}\n".format(average_change_in_profit_loss)
str4 = "Greatest Increase in Profits: {0} (${1})\n".format(month[max_position], change_in_profit_loss[max_position])
str5 = "Greatest Decrease in Profits: {0} (${1})\n".format(month[min_position], change_in_profit_loss[min_position])

textfile = open("Financial_Analysis.txt", "w")
textfile.write("Financial Analysis\n")
textfile.write("----------------------------\n")
textfile.write(str1)
textfile.write(str2)
textfile.write(str3)
textfile.write(str4)
textfile.write(str5)
textfile.close()

