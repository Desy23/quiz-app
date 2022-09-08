quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    }
},

score =

for key, value in quiz.items():
    print(value['question'])
answer = input("Your answer: ")

if answer.lower == value['answer'].lower():
    print("Correct!")
score = score + 1
print("Your scored is: " + str(score))

else:
print("Wrong")
