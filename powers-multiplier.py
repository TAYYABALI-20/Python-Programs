n = int(input("Enter a number (n): "))

maxPower = int(input("\nEnter the maximum power (Max Power): "))

print(f"\n{'n':<10} {'Power':<10} {'n raised to power':<10}")

print('-'*39)

power = 0

while power <= maxPower:
    
    result = n ** power
    
    print(f"{n:<10} {power:<10} {result:<10}")
    
    power += 1