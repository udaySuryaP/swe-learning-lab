monthlyExpense = [2200, 2350, 2600, 2130, 2190]

# 1
print(
    f"February extra expenditure when compared to January: {monthlyExpense[1]-monthlyExpense[0]}")

# 2
quarterExpense = 0
for i in range(3):
    quarterExpense += monthlyExpense[i]
print(f"Quarterly Expense: {quarterExpense}")

# 3
for expense in range(len(monthlyExpense)):
    if (monthlyExpense[expense] == 2000):
        print(f"Month with exact 2000 spend is: {expense + 1}")

#4
monthlyExpense.append(1980)
print(f"June Expense Updated \n{monthlyExpense}")

#5
monthlyExpense[3] -=200
print(f"Refund amount deducted from April Expense \n{monthlyExpense}")


'''
monthlyExpense = {
    "January":2200,
    "February": 2350,
    "March":2600,
    "April":2130,
    "May":2190
}

#1
print(monthlyExpense["February"] - monthlyExpense["January"])


#2
quarterlyExpense = 0
mExpense = list(monthlyExpense.values())
for i in range(3):
    quarterlyExpense += mExpense[i]

print(f"Quarterly Expense: {quarterlyExpense}")


#3
for month, expense in monthlyExpense.items():
    if(expense == 2000):
        print(f"Month with exact 2000 spent: {month}")


#4
monthlyExpense["June"] = 1980
print(monthlyExpense)


#5
monthlyExpense["April"] -= 200
print(monthlyExpense)
'''
