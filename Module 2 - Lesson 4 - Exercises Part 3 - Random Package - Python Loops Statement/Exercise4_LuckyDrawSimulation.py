import random

participants = ["John", "Lila", "Sarah", "Alex", "Max"]

while "Alex" not in random.choices(participants, k=1):
    pass
print("Congratulations, Alex! You've won the lucky draw!")