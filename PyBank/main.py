#Dependencies 
import csv
import os

#Files
file_input = os.path.join("Resources", "budget_data.csv") 
file_output = os.path.join("Analysis" , "Results.txt")

#setting parameters
total_number_months = 0
net_total_amount = 0
average_change = []
month_change = []
greatest_increase_amount = ["", 0]
geatest_decrease_amount = ["", 9999999999999999]


with open(file_input) as finance_data:
    reader = csv.reader(finance_data)
    header = next(reader)


    first_row = next(reader)
    total_number_months += 1
    net_total_amount += int(first_row[1])
    prior_net_total_amount = int(first_row[1])

    for row in reader:

        # calculating the totals
        total_number_months += 1
        net_total_amount += int(row[1])

        #calculating the average changes
        net_average = int(row[1]) - prior_net_total_amount
        prior_net_total_amount = int(row[1])
        average_change += [net_average]
        month_change += [row[0]]


        #getting increases and decreases 
        if net_average > greatest_increase_amount[1]:
            greatest_increase_amount[0] = row[0]
            greatest_increase_amount[1] = net_average

        if net_average < geatest_decrease_amount[1]:
            geatest_decrease_amount[0] = row[0]
            geatest_decrease_amount[1] = net_average

#getting the average
monthly_average = sum(average_change) / len(average_change)

#Summary
output = (
        f"Finacial Analysis\n"
        f"=================================================================\n"
        f"Total Months: {total_number_months}\n"
        f"Totals: {prior_net_total_amount}\n"
        f"Average Change: ${monthly_average:.2f}\n"
        f"Greatest Increase in Profit: {greatest_increase_amount[0]} (${greatest_increase_amount[1]})\n"
        f"Greatest Decrease in Profit: {geatest_decrease_amount[0]} (${geatest_decrease_amount[1]})\n"
         )

print(output)

with open(file_output, "w") as txt_file:
    txt_file.write(output)



