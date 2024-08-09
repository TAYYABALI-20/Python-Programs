user_name = str(input('What is your name? '))

favourite_places = {1: 'Taj Mahal', 2: 'Mohenjo Daro', 3: 'Minar-e-Pakistan'}

print(f'\n{user_name} likes the following places:')

for place in favourite_places:
    
    print(f'{place}: {favourite_places[place]}')