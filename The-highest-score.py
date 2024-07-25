# Input a list of student scores

student_scores = input("Enter a list of student scores : ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

The_highest_score = 0
for score in student_scores :
  if The_highest_score < score :
    The_highest_score = score

print(f'The highest score in the class is: {The_highest_score}')


