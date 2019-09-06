import os
import csv
bank_csv = os.path.join(".","Resources","budget_data.csv")
months = 0
net_profit_loss = 0
total_change = 0
greatest_profit = 0
greatest_profit_month = ""
greatest_loss = 0
greatest_loss_month = ""
last_profit_loss = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""
with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        month = row[0]
        months = months + 1
        profit_loss = int(row[1])
        net_profit_loss += profit_loss
        if (months == 1):
            profit_loss_change = 0
        else:
            profit_loss_change = profit_loss - last_profit_loss
        total_change += profit_loss_change
        if (profit_loss < greatest_loss):
            greatest_loss = profit_loss
            greatest_loss_month = month
        else:
            if (profit_loss > greatest_profit):
                greatest_profit = profit_loss
                greatest_profit_month = month
        if (profit_loss_change < greatest_decrease):
            greatest_decrease = profit_loss_change
            greatest_decrease_month = month
        else:
            if (profit_loss_change > greatest_increase):
                greatest_increase = profit_loss_change
                greatest_increase_month = month
        last_profit_loss = profit_loss
average_profit_loss = round(net_profit_loss/months,2)
average_change = round(total_change/(months-1),2)
print("------------------")
print("Financial Analysis")
print("------------------")
print(f"Total Months: {months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Profit/Loss: ${average_profit_loss}")
print(f"Greatest Profit: {greatest_profit_month} ${greatest_profit}")
print(f"Greatest Loss: {greatest_loss_month} ${greatest_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase: {greatest_increase_month} ${greatest_increase}")
print(f"Greatest Decrease: {greatest_decrease_month} ${greatest_decrease}")
filename = "Pybank.txt"
with open(filename, 'w') as f:
    f.write("------------------")
    f.write("Financial Analysis")
    f.write("------------------")
    f.write(f"Total Months: {months}")
    f.write(f"Total: ${net_profit_loss}")
    f.write(f"Average Profit/Loss: ${average_profit_loss}")
    f.write(f"Greatest Profit: {greatest_profit_month} ${greatest_profit}")
    f.write(f"Greatest Loss: {greatest_loss_month} ${greatest_loss}")
    f.write(f"Average Change: ${average_change}")
    f.write(f"Greatest Increase: {greatest_increase_month} ${greatest_increase}")
    f.write(f"Greatest Decrease: {greatest_decrease_month} ${greatest_decrease}")