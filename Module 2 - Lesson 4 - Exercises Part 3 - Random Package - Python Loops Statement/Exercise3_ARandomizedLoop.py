import random

snacks = ["apple", "banana", "carrot stick", "doughnut", "chocolate bar"]
picked_snack = ''

while picked_snack != "chocolate bar":
    picked_snack = random.choice(snacks)
    print(f"You got a {picked_snack}.")
    if picked_snack != "chocolate bar":
        print("Let's pick again!")
    else:
        print("Yay! Chocolate bar wins!")