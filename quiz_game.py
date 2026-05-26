questions = ["What is the capital of India?",
    "Which language is used for AI?",
    "How many days are there in a week?"]
answers = ["delhi","python","7"]
score = 0
for i in range(len(questions)):
    print("Question", i + 1)
    user_answer = input(questions[i] + " ")
    if user_answer.lower() == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("The correct answer is:", answers[i])
percentage = (score / len(questions)) * 100
if percentage >= 90:
    grade = "Excellent"
elif percentage >= 70:
    grade = "Good"
elif percentage >= 50:
    grade = "Average"
else:
    grade = "Improve"
print("======================================")
print("Quiz Over!")
print("Your final score is:", score)
print("Your percentage is:", round(percentage, 3), "%")
print("Your grade is:", grade)