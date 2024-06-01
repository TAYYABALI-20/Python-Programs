#Write a Python program that asks the user to input 10 numbers. 
#The program should then determine how many of these numbers are even and how many are odd. 
#Finally, display the count of even and odd numbers to the user.

even_count = 0
odd_count = 0

for i in range (1, 11):
     
     print(f"Let's find out how many even and odd numbers you can provide! Please enter {i}/10 number:")
     
     number = int(input())
     
     if number % 2 == 0:
          even_count += 1
     else:
          odd_count += 1

print(f"You entered {even_count} even numbers and {odd_count} odd numbers.")