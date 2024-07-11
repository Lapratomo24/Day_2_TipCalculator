# Tip Calculator

# how to split a bill + tip between multiple people
# then round the amount with 2 decimal places

bill = float(input("How much is the dinner bill? \n$"))
tip = int(input("How much is the tip? 5, 10, or 15?\n")) #percentage
people = int(input("How many people is it split between?\n"))

percentage = tip / 100
bill_amount = bill * percentage
total_amount = bill + bill_amount
split_amount = total_amount / people

print(f"The total amount plus tip is ${split_amount:.2f}")

# alternative
# amount = round(split_amount, 2)
