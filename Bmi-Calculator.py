print("Welcome to the Bmi Calculator")
# 1st input: enter height in meters
height = input("enter height in meters : ")
# 2nd input: enter weight in kilograms 
weight = input("enter weight in kilograms : ")

new_weight = float(weight)
new_height = float(height)**2
Bmi = new_weight / new_height

print(int(Bmi))

# Or you can simply use the round function : 
# print(round(Bmi))

