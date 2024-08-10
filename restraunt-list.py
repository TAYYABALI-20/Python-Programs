# Print the user ordered food from the list

restraunt_list = [['Ahsan','Biryani'],['Tayyab','Kabab'],['Muslim','Cigaratte'],['Bobby','Pizza']]

def food_func(food):
    
    message = ''
    
    for item in food:
        
        message += f'Dear {item[0]}, thanks for ordering {item[1]}.\n'
        
    return message    

print(food_func(restraunt_list))