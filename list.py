import random
programming_language = ["Python","JavaScript","C++","Ruby","Java"]  
difficulty_level = [2,3,4,2,5]

quiz_data = list(zip(programming_language, difficulty_level))

random.shuffle(quiz_data)
score = 0
for language,difficulty in quiz_data:
    guess =int(input(f"What is the difficulty level of {language}?(Enter a number from 1-5)"))
    if guess == difficulty:
        print("Correct")
        score += 1
    else:
        print(f"No retard {language} is {difficulty} out of 5 ")       
print(f"\nQuiz Complete your score was {score}/5")
