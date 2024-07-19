print("Welcome to the Tip Calculator!")

total_bill = input("What was The total bill? $")

tip = input("How much tip you like to give ? 10, 12, or 15? ")

people_num = input("How many people to split the bill? ")

new_total_bill = round(float(total_bill) * int(tip) / 100 + float(total_bill), 2)

each_person_pay = round(new_total_bill / int(people_num), 2)

print(f"Each preson shoold pay : ${each_person_pay}.")




