import random

quiz_questions = ["What is the capital of France", "What is 2+2?", "What is the boiling point of water?"]

random.shuffle(quiz_questions)

for questions in quiz_questions:
    print(questions)