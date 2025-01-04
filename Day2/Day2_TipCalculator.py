print("Welcome to the tip calculator!")
bill = float(input("What was the total bil? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12 or 15? "))
total_people = input("How many people to split the bill? ")
total_bill_with_tip = bill + ((bill * tip_percent) / 100)
per_person_bill = round(total_bill_with_tip / int(total_people), 2)
print(f"Each person should pay: ${per_person_bill}")
# print(total_bill)



