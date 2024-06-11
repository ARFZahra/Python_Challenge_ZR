import csv
import os

# Input path
csvpath = os.path.join(".", "Resources", "budget_data.csv")

def analyze_budget_data(Budget_data):
    # Initialize variables
    profit_losses = []
    dates = []
    total_months = 0
    net_total_amount = 0
    
    with open(Budget_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # Read the header row first
        csv_header = next(csvreader)

        # Read the first row except header and initialize with the first row
        first_row = next(csvreader)
        dates.append(first_row[0])
        profit_losses.append(int(first_row[1]))
        total_months += 1
        net_total_amount += int(first_row[1])
        
        # Read each subsequent row of data after the first row
        for row in csvreader:
            dates.append(row[0])  # Extract the date and append it to the dates list
            profit_loss = int(row[1])
            profit_losses.append(profit_loss)  # Extract the profit/loss value, and append to the profit_losses list
            net_total_amount += profit_loss
            total_months += 1
        
        # Used list comprehension to calculate the month-to-month changes in profit/loss 
        #(used Xpert learning assitant and chatgtp to understand and  write list comprehension code and to find max and min profit changes)
        changes = [profit_losses[i] - profit_losses[i-1] for i in range(1, len(profit_losses))] 

        # The average of the changes in "Profit/Losses" over the entire period
        average_change = sum(changes) / len(changes)

        # Find the greatest increase and decrease in profits 
        greatest_increase = max(changes)
        greatest_decrease = min(changes)
        greatest_increase_month = dates[changes.index(greatest_increase) + 1]
        greatest_decrease_month = dates[changes.index(greatest_decrease) + 1]

    # Return analysis as a dictionary
    return {"Total Months": total_months,"Total": net_total_amount,"Average Change": average_change,"Greatest Increase in Profits": (greatest_increase_month, greatest_increase),
        "Greatest Decrease in Profits": (greatest_decrease_month, greatest_decrease)}

# Analyze budget data
analysis = analyze_budget_data(csvpath)

# Output the results to the console
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {analysis['Total Months']}")
print(f"Total: ${analysis['Total']}")
print(f"Average Change: ${analysis['Average Change']:.2f}")
print(f"Greatest Increase in Profits: {analysis['Greatest Increase in Profits'][0]} (${analysis['Greatest Increase in Profits'][1]})")
print(f"Greatest Decrease in Profits: {analysis['Greatest Decrease in Profits'][0]} (${analysis['Greatest Decrease in Profits'][1]})")

# Path to the output file
output_file_path = os.path.join(".", "Analysis", "budget_output.txt")

# Write the results to a text file (used Xpert learning assitant and chatgtp to understand and writing the output file in .txt file)
with open(output_file_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Months: {analysis['Total Months']}\n")
    txtfile.write(f"Total: ${analysis['Total']}\n")
    txtfile.write(f"Average Change: ${analysis['Average Change']:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {analysis['Greatest Increase in Profits'][0]} (${analysis['Greatest Increase in Profits'][1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {analysis['Greatest Decrease in Profits'][0]} (${analysis['Greatest Decrease in Profits'][1]})\n")

