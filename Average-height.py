
student_heights = input("Enter python list of student height in centimeters:").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height2 = 0
for total_height in student_heights :
  total_height2 += total_height
print(f"total height = {total_height2}")

number_of_students = n + 1
print (f"number of students = {number_of_students}")

average_height = round(total_height2 / number_of_students)
print(f"average height = {average_height}")



