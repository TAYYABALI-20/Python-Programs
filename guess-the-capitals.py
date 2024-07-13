print('Welcome to our Python Guess The Capitals Program.')

countriesCapitals = {'Russia': 'Moscow', 'Germany': 'Berlin', 'Spain': 'Madrid', 'Ukraine': 'Kiev', 'Italy': 'Rome'}

for country in countriesCapitals:
    
    answer = input(f"\nWhat is the capital of {country}? ")
    
    if answer.strip().lower() == countriesCapitals[country].lower():
        print("\nCorrect!")

    else:
        print(f"\nWrong! The capital of {country} is {countriesCapitals[country]}.") 