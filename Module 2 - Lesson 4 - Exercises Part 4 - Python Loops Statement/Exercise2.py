inventory = ["Apples", 120, "Oranges", 80, True, "Bananas", 150, False]

index = 0

while index < len(inventory):
    item = inventory[index]

    if type(item) == str:
        print(f"Item: {item}")
    elif type(item) == int:
        print(f"Quantity: {item}")
    elif type(item) == bool:
        status = "on sale" if item else "not on sale"
        print(f"Sale status: {status}")

    index += 1