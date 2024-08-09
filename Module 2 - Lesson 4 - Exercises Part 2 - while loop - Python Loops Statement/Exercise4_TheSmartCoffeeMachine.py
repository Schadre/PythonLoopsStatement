coffee_reservoir = 10
coffee_types = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha"]

while coffee_reservoir > 0:
    if coffee_types:
        current_coffee = coffee_types.pop(0)
        print(f"Dispensing {current_coffee}.")
        coffee_reservoir -= 1
        print(f"Coffee types left: {coffee_types}")
    else:
        print("No more coffee types available.")
        break
print("The coffee reservoir is now empty")