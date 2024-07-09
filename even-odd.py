#Write a Python program that asks the user to input a number. 
#The program should then determine whether the entered number is even or odd a
#nd display an appropriate message to the user.

number = int(input("Please enter a number, and we'll let you know if it's even or odd: "))

if number % 2 == 0 :
    print(f"Great choice! The number {number} is even.")
else:
     print(f"Great choice! The number {number} is odd.")