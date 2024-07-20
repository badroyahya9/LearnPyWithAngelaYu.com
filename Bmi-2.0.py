# Enter your height in meters 
height = float(input("Enter your height in meters :"))
# Enter your weight in kilograms 
weight = int(input("Enter your weight in kilograms :"))

# Code below this line 👇

Bmi = weight / height ** 2 

if Bmi < 18.5 :
  print (f"Your BMI is {Bmi}, you are underweight.")
elif Bmi >= 18.5 and Bmi < 25 :
  print (f"Your BMI is {Bmi}, you have a normal weight.")
elif Bmi >= 25 and Bmi < 30 :
  print (f"Your BMI is {Bmi}, you are slightly overweight.")
elif Bmi >= 30 and Bmi < 35 :
  print (f"Your BMI is {Bmi}, you are obese.")
else :
  print (f"Your BMI is {Bmi}, you are clinically obese.")
