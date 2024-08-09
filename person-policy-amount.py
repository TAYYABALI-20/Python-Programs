print('Welcome to our Python Policy Amount Calculator. \n')

personGender = str(input('Please enter your gender here (Male/Female): ')).strip().lower()

personName = str(input('\nPlease enter your name here: '))

personAge = int(input(f'\nDear {personName}, please enter your age here: '))

personHealth = str(input(f"\nDear {personName}, How's your health these days (Excellent/poor)?: ")).strip().lower()

personResidency = str(input(f"\nDear {personName}, where do you live (City/Village)?: ")).strip().lower()

if personHealth == 'excellent' and personAge >= 25 and personAge <= 34 and personResidency == 'city' and personGender == 'male':
    print(f"\nDear {personName}, your premium rate is 4 per thousand, and your policy amount cannot exceed Rs 2 Lakh.")
elif personHealth == 'excellent' and personAge >= 25 and personAge <= 34 and personResidency == 'city' and personGender == 'female':
    print(f"\nDear {personName}, your premium rate is 3 per thousand, and your policy amount cannot exceed Rs 1 Lakh.")
elif personHealth == 'poor' and personAge >= 25 and personAge <= 35 and personResidency == 'village' and personGender == 'male':
    print(f"\nDear {personName}, your premium rate is 6 per thousand, and your policy amount cannot exceed Rs 10,000.")
else:
    print(f'\nDear {personName}, sorry to say but we can not insured you the policy ammount since you are not fit to our criteria.')