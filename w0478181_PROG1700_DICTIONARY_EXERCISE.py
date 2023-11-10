#W0478181
#Repository: <https://github.com/W0478181/PROG1700Assignments>
#Date Nov 9,2023
#Dictionary
student_scores = {}

#Info
student_scores = {
    "Bryan": 90,
    "Hotdog man": 85,
    "Bryce": 78,
    "Mr Hands": 92,
    "Joe": 88
}

print("Student Scores:")
for student, score in student_scores.items():
    print(f"{student}: {score}")

# Class Average
average_score = sum(student_scores.values()) / len(student_scores)
print(f"\nAverage Test Score: {average_score}")

# Chose student to see score
student_name = input("\nEnter a student's name to check their score: ")
if student_name in student_scores:
    print(f"{student_name}'s score is {student_scores[student_name]}")
else:
    print(f"Student {student_name} not found in the records.")

# Change a students score
update_student = input("\nEnter the name of the student to update their score: ")
if update_student in student_scores:
    new_score = int(input(f"Enter {update_student}'s new score: "))
    student_scores[update_student] = new_score
    print(f"{update_student}'s score has been updated to {new_score}")
else:
    print(f"Student {update_student} not found in the records.")

# Chose student to remove
remove_student = input("\nEnter the name of the student to remove: ")
if remove_student in student_scores:
    del student_scores[remove_student]
    print(f"{remove_student} has been removed from the records.")
else:
    print(f"Student {remove_student} not found in the records.")

# Who had the highest score?
highest_score = max(student_scores, key=student_scores.get)
print(f"\nHighest Score: {student_scores[highest_score]} achieved by {highest_score}")

# New class Average
average_score = sum(student_scores.values()) / len(student_scores)
print(f"\nAverage Test Score: {average_score}")
