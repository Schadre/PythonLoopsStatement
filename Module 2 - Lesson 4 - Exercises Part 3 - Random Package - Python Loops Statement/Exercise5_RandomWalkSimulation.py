import random

directions = ["North", "South", "East", "West"]

for step in range(10):
    step_direction = random.choice(directions)
    print(f"Step {step + 1}: The entity moves 10 steps to the {step_direction}")