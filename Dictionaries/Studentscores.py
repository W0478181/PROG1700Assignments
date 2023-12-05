# Step 1
student_scores = {}

# Step 2
student_scores = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 78,
    "David": 92,
    "Eve": 88
}

# Step 3
print("Student Scores:")
for student, score in student_scores.items():
    print(f"{student}: {score}")

# Step 4
average_score = sum(student_scores.values()) / len(student_scores)
print(f"\nAverage Test Score: {average_score}")

# Step 5
student_name = input("\nEnter a student's name to check their score: ")
if student_name in student_scores:
    print(f"{student_name}'s score is {student_scores[student_name]}")
else:
    print(f"Student {student_name} not found in the records.")

# Step 6
update_student = input("\nEnter the name of the student to update their score: ")
if update_student in student_scores:
    new_score = int(input(f"Enter {update_student}'s new score: "))
    student_scores[update_student] = new_score
    print(f"{update_student}'s score has been updated to {new_score}")
else:
    print(f"Student {update_student} not found in the records.")

# Step 7
remove_student = input("\nEnter the name of the student to remove: ")
if remove_student in student_scores:
    del student_scores[remove_student]
    print(f"{remove_student} has been removed from the records.")
else:
    print(f"Student {remove_student} not found in the records.")

# Step 8
highest_score = max(student_scores.values())
highest_scorer = [student for student, score in student_scores.items() if score == highest_score][0]
print(f"\nHighest Score: {highest_score} achieved by {highest_scorer}")
