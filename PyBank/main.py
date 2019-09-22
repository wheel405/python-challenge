# This is main.py in PyBank
import os
import csv

#path to correct csv file
csvpath = os.path.join('Resources/budget_data.csv')

#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period

#define variables: total number of months in dataset
total_months = 0
total_revenue = 0
change_list=[]
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = 0
greatest_decrease_month = 0




#open CSV reader to read budget_data.csv
with open(csvpath)as financial_data:
    reader=csv.reader(financial_data)
    header = next(reader)
    first_row = next(reader)
    first_value= int(first_row[1])
    total_months = total_months + 1
   
#Find changes from month to month and the average gain or loss
    for row in reader:
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])
        change = int(row[1])-first_value
        first_value = int(row[1])
        change_list.append(change)

average_change = sum(change_list)/len(change_list)
#Find the greatest increase in profits (date and amount) over the entire period
if int(row[1]) > greatest_increase:
    greatest_increase=int(row[1])
    greatest_increase_month=row[0]
if int(row[1]) < greatest_decrease:
    greatest_decrease=int(row[1])
    greatest_decrease_month=row[0]
    
print("----Financial Analysis----")
print(" Total Months: " + str(total_months))
print(" Total Revenue: $" + str(total_revenue))
print(" Average Change: $" + str(average_change))
print(" Greatest Gain: $" + str(greatest_increase))
print(" Greatest Loss: $" + str(greatest_decrease))
