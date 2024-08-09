battery = 0
increment = 10

while battery < 100:
    battery += increment
    print(f"Battery is now at {battery}%")

    if battery == 50:
        print("Efficiency check: Increasing charge rate.")
        increment = 15
    elif battery == 80:
        print("Efficiency check: Reducing charge rate prevent overcharging.")
        increment = 5

print("The battery is now fully charged.")