print("Welcome to the tip calculator.")
bill = input("What was the total bill $")
tip_percentage = input("How much percentage of tip would you like to give? 10, 12, or 15?")

people = input("How much people would split the bill?")

tip = float(bill)*float(tip_percentage)/100
total_bill = float(bill)+tip

split = total_bill/int(people)

print(f"Each person should pay: ${round(split,2)}")