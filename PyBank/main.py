    PyBank:

Assignment Instructions:
    Create a Python script that analyzes the financial records of your company.

    Analyze the records to calculate the following values:
            - Total number of months included in the dataset
            - Net total amount of "Profit/Losses" over the entire period
            - Changes in "Profit/Losses" over the entire period, and then the average of those changes
            - Greatest increase in profits (the date and amount) over the entire period
            - Greatest decrease in profits (the date and amount) over the entire period

//////


#   Import the os and csv modules
import os
import csv


#   Set and open file with the csv library
csvpath = os.path.join('C:\Users\emich\Desktop\penn data science bootcamp\Mod3_Assignment\python-challenge\PyBank\Resources', 'budget_data.csv')

#   Define your variables
totnum_months = 0
net_tot = 0
greatest_inc = {"month": "". "value": 0}
greatest_dec = {"month": "", "value": 0}
monthly_change = 0
prev_value = 0
profit_change = 0

#   Read the csv file, split on commas, account for the header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        #profit_loss = int(row[1])

        #   Formula for Total number of months (totnum_months)
        totnum_months = totnum_months + 1

        #   Formula for the net profits, or the sum of all the profits and losses (net_tot)
        net_tot = net_tot + int(row[1])

        #   Conditional for the greates increase and decrease (greatest_inc and greatest_dec)
        if greatest_inc["value"] < int(row[1]):
            greatest_inc["month"] = row[0]
            greatest_inc["value"] = int(row[1])
        if greatest_dec["value"] > int(row[1]):
            greatest_dec["month"] = row[0]
            greatest_dec["value"] = int(row[1])

        
            # Count the average changes for the entire period
        profit_change = int(row[1]) - prev_value
        monthly_change.append(profit_change)
        prev_value = int(row[1])


        #   Calculate the average change (of those changes)
        average_change = sum(monthly_change)/totnum_months

        #   Filter data into analysis to reflect the results located on instructions
        output = (
            f"Financial Analysis\n"
            f"-----------------------\n"
            f"Total Number of Months: {totnum_months}\n"
            f"Total: ${net_tot}\n"
            f"Average Change: ${round(average_change, 2)}\n"
            f"Greatest Increase in Profits: {greatest_inc['month']} (${greatest_inc['value']})\n"
            f"Greatest Decrease in Profits: {greatest_dec['month']} (${greatest_dec['value']})\n"
        )

        #   Print the outputs to the terminal
        print(output)

        #   Print out the outputs into the txt file within the analysis folder of the PyBank folder
        with open("PyBank\Analysis\output.txt", "w") as txt_file:
            txt_file.write.output