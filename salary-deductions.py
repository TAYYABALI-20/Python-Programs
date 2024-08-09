#Write a Python program that prompts the user to input their monthly salary, 
#the percentage of their salary spent on house rent, and the percentage spent 
#on other expenses. The program should then calculate and display the amount 
#spent on house rent, the amount spent on other expenses, 
#and the remaining salary after these deductions.

userSalary = int(input('Hey there! Could you please enter your monthly salary? Thanks!'))
userHouseRent = int(input('Now, could you please enter the percentage of your salary spent on house rent? Thanks!'))
userOtherExpenses = int(input('Finally, could you please enter the percentage of your salary spent on other expenses? Thanks!'))

houseRent = userSalary * userHouseRent / 100
otherExpenses = userSalary * userOtherExpenses / 100
remainingSalary = userSalary - houseRent - otherExpenses

print(f'Your house rent is {houseRent}')
print(f'Your other expenses is {otherExpenses}')
print(f'Your remaining salary is {remainingSalary}')