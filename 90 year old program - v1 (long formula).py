# -------------------------------------------------------------------------#
# Program: How much time left do you have, if you live until 90 years old?
# -------------------------------------------------------------------------#

age = input("What is your current age? ")

# 90 years converted in days, weeks, months
days = 365
weeks = 52
months = 12

# --- Formulas ---
# Days
totalDays = days * int(90)
currentUserDays = int(age) * int(days)
daysRemaining = totalDays - currentUserDays
# Weeks
totalWeeks = weeks * int(90)
currentUserWeeks = int(age) * int(weeks)
weeksRemaining = totalWeeks - currentUserWeeks
# Months
totalMonths = months * int(90)
currentUserMonths = int(age) * int(months)
monthsRemaining = totalMonths - currentUserMonths

# Output The Message
message = f"\nYou have {daysRemaining} days, {weeksRemaining} weeks, {monthsRemaining} months, until you reach 90 years old"
print(message)