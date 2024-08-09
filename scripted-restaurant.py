scriptedEveryBite = ('Pizza', 'Burger', 'Macaroni', 'Grilled Chicken', 'Fish')

print("Original Menu:")

for bite in scriptedEveryBite:
    
    print(bite)

print('\nScripted Restaurant Has Changed Their Menu.')

changedMenu = list(scriptedEveryBite)

changedMenu[3] = 'Cheese Fries'

changedMenu[4] = 'Steaks'

newMenu = tuple(changedMenu)

print("\nNew Menu:")

for bite in newMenu:
    
    print(bite)