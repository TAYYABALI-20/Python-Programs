# Write a Python program that asks the user for their years of service and qualification, 
# then calculates the salary based on the provided criteria.

yearsOfService = int(input("Enter your years of service: "))

qualification = input("Enter your qualification (Masters/Bachelors): ")

salary = 0

if yearsOfService >= 10:
    
    if qualification.lower() == "masters":
        salary = 150000
    
    elif qualification.lower() == "bachelors":
        salary = 100000

else:
    
    if qualification.lower() == "masters":
        salary = 100000
    
    elif qualification.lower() == "bachelors":
        salary = 70000

print(f"Your calculated salary is: {salary}")