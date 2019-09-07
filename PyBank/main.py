#!/usr/bin/env python
# coding: utf-8

# In[1]:


#set input filepath
import os
import csv
bank_csv = os.path.join(".","Resources","budget_data.csv")


# In[2]:


#initialize variables
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


# In[3]:


#read csv and analyze rows
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


# In[4]:


def print_and_save(message,f):
    print(message)
    f.write(f"{message}\n")


# In[6]:


#print and save analysis
filename = "Pybank.txt"
with open(filename, 'w') as f:
    print_and_save("------------------",f)
    print_and_save("Financial Analysis",f)
    print_and_save("------------------",f)
    print_and_save(f"Total Months: {months}",f)
    print_and_save(f"Total: ${net_profit_loss}",f)
    print_and_save(f"Average Profit/Loss: ${average_profit_loss}",f)
    print_and_save(f"Greatest Profit: {greatest_profit_month} ${greatest_profit}",f)
    print_and_save(f"Greatest Loss: {greatest_loss_month} ${greatest_loss}",f)
    print_and_save(f"Average Change: ${average_change}",f)
    print_and_save(f"Greatest Increase: {greatest_increase_month} ${greatest_increase}",f)
    print_and_save(f"Greatest Decrease: {greatest_decrease_month} ${greatest_decrease}",f)

