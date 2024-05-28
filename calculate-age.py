#Write a program to calculate your age

myName = str(input('Please enter your name here.'))

myBirthYear = int(input('Please enter your birth year here.'))

currentYear = int(input('Please enter the current year here.'))

myAge = currentYear - myBirthYear

print('Dear',myName,'Your Age Is',myAge)