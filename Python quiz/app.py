#dictionary that store both questions and answers

quiz_questions = {
    "Question 1": {
        "question": "What is the output of the following code?\nprint(2 + 3 * 4 - 8)",
        "answer": "six"
    },
    "Question 2": {
        "question": "Which keyword is used to define a function in Python?",
        "answer": "def"
    },
    "Question 3": {
        "question": "What is the correct way to comment multiple lines in Python?",
        "answer": "Use triple quotes (''' or \"""\) at the beginning and end of the block."
    },
    "Question 4": {
        "question": "What is the output of the following code?\nprint('Hello' + 'World')",
        "answer": "HelloWorld"
    },
    "Question 5": {
        "question": "Which data structure in Python is an ordered, mutable, and indexed collection?",
        "answer": "List"
    },
    "Question 6": {
        "question": "What is the syntax to open a file named 'data.txt' in read mode in Python?",
        "answer": "file = open('data.txt', 'r')"
    },
    "Question 7": {
        "question": "Which module in Python is used for working with dates and times?",
        "answer": "datetime"
    },
    "Question 8": {
        "question": "What is the output of the following code?\nprint(type(42.0))",
        "answer": "<class 'float'>"
    },
    "Question 9": {
        "question": "Which operator is used to perform exponentiation in Python?",
        "answer": "**"
    },
    "Question 10": {
        "question": "What is the correct way to check if a key exists in a dictionary in Python?",
        "answer": "Use the 'in' keyword. For example, 'if key in my_dict:'"
    }
}

score = 0

for key, value in quiz_questions.items():
    print(value['question'])
    answer = str(input("Answer? "))

    if answer.lower() == value['answer'].lower():
        print("CORRECT  :) ")
        score += 1
        print("Your score is: " + str(score))

    else:
        print("WRONG :( ")
        print("The correct answer is: " + value['answer'])

print("You got " + str(score) + " out of 10 questions correctly.")
print("Your percentage is " + str(score/len(quiz_questions) * 100) + "%.")
