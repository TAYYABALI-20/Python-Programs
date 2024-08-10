# Define a function called “calculate_bill” that takes one argument food as input. In the
# function, create a variable total with an initial value of zero. For each item in the food list,
# add the price of that item to total. In the end, return the total as output.

food_list = [
    ['Tomato', 19],
    ['Apple', 75],
    ['Milk', 220],
    ['Barbecue Sauce', 10],
    ['Mutton', 650]
]

def calculate_bill(food):
    
    total = 0
    
    for item in food:
        
        total += item[1]
    
    return total

bill = calculate_bill(food_list)

print(f'Your Current Bill = {bill} PKR.')