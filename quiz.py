def run_quiz(questions):
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct answer is:", q["answer"])

    print("\nQuiz Finished!")
    print("Your Score:", score, "/", len(questions))


def main():
    questions = [
        {
            "question": "1. What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "2. Which language is used for web development?",
            "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
            "answer": "B"
        },
        {
            "question": "3. Which keyword is used to define a function in Python?",
            "options": ["A. func", "B. def", "C. function", "D. define"],
            "answer": "B"
        }
    ]

    run_quiz(questions)

main()
