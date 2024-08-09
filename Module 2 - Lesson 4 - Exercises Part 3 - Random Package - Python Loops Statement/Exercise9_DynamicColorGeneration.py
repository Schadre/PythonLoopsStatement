import random

num_colors = 10

for _ in range(num_colors):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    print(f"Generated RGB color ({red}, {green}, {blue})")