# Make the following changes to your calculate_bill function: While you loop through each
# item of food, only add the price of the item to total if the item price is greater than 20.
# Also add 3 more items in your grocery items and remove 2 less price items in your
# previous groceries item.

food_list = [
    ['Tomato', 19],
    ['Apple', 75],
    ['Milk', 220],
    ['Barbecue Sauce', 10],
    ['Mutton', 650]
]

def calculate_bill(food):
    
    total = 0
    
    food_list.insert(5, ['Ketchup', 35])
    food_list.insert(6, ['Yogurt', 100])
    food_list.insert(7, ['Chicken Roll', 110])
    
    for item in food:
        
        if item[1] > 20:
            total += item[1]
        else:
            del item
    
    return total

bill = calculate_bill(food_list)

print(f'Your Current Bill = {bill} PKR.')