


questions = ("How many elements are in the periodic table:",
             "Which animal lays the largest eggs:",
             "What is the most abundant gas in Earth's atmosphere:",
             "How many bones are in a human body:",
             "Which planet in the solar system is the hottest:")

options = (('A.116', 'B.117', 'C.118', 'D.119'),
           ('A.Whale', 'B.Crocodile', 'C.Elephant', 'D.Ostrich'),
           ('A.Nitrogen', 'B.Oxygen', 'C.Carbon-Dioxide', 'D.Hydrogen'),
           ('A.206', 'B.207', 'C.208', 'D.209'),
           ('A.Mercury', 'B.Venus', 'C.Earth', 'D.Mars'))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

print("Welcome to the Quiz Game!")
print("Answer the following questions:\n")

for i, question in enumerate(questions):
    print("------------------")
    print(f"Question {i + 1}: {question}")

    for option in options[i]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[i]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print(f"The correct answer is {answers[i]}")

    print()

print("-------------------")
print("      RESULTS      ")
print("-------------------")

print("Your answers: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print(f"Your score: {score}/{len(questions)}")
print(f"Percentage: {int(score / len(questions) * 100)}%")

# Optional: Show which questions were right/wrong
print("\nQuestion Breakdown:")
for i in range(len(questions)):
    status = "✓" if guesses[i] == answers[i] else "✗"
    print(f"Q{i + 1}: Your answer: {guesses[i]} | Correct: {answers[i]} {status}")