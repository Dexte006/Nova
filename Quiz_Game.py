# quiz game

questions = ("What is the largest organ in the human body?",
             "What is the chemical symbol for gold?",
             "Which planet is known as the Red Planet?", 
             "What is the process by which plants convert sunlight into energy?", 
             "What is the largest land animal on Earth?", "What is the smallest unit of matter?")

options = (("A. The Heart", "B. The liver", "C. The Brain", "D. The Skin"),
           ("A. Au", "B. Ag", "C. Fe", "D. Hg"),
           ("A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"),
           ("A. Photosynthesis", "B. Respiration", "C. Transpiration", "D. Fertilization"),
           ("A. Elephant", "B. Giraffe", "C. Hippopotamus", "D. Blue Whale"),
           ("A. Atom", "B. Molecule", "C. Cell", "D. Proton"))

answers = ("D","A","A","A","A","A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score = score + 1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is correct answer")

    question_num = question_num + 1



print("-------------------------")
print("         RESULT          ")
print("-------------------------")

print("answers: ",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()


score =int(score / len(questions) * 100)
print(f"Your score is: {score}%")
