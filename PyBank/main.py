# the total of months included in the dataset
import datetime
date = datetime.date("january","December")
month_number = date.month
print (date)
print (f"month number is:{month_number}")


# the net total of "Profit/Losses" over the entire period
total_income = sum(income)
total_losses = sum(losses)
if net_profit_loss> 0:
    result = "profit"
elif net_profit_loss<0:
    result ="losses"
else:
    result = "neither profit nor losses"

# the changes in "profit/Losses" ove entire period, and then  the of those changes
net_profit_losses=0
profit_losses_over_time = [12 months]
for i in range(income):
    netprofit_loss+=income[i] - losses[i]
    profit_losses_over_time.append(net_profit_losses)

# the greatest increase in profits (date and amount) over the entire period
if net_profit_losses> max_increase:
    max_increase = nne_profit_losses
    max_increase_date=dates[i]
    print(f"the greates increase in profit")


# the greatest Decrease in profits (date and amount) over the entire period
if net_profit_losses> max_increase:
    max_decrease = nne_profit_losses
    max_decrease_date=dates[i]
    print(f"the greates decrease in profit")
