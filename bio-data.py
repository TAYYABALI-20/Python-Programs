# Write a program to print a student’s bio data having his/her Date of birth, Roll no,
# Section, Percentage and grade of matriculation and Intermediate. All the fields should
# be entered from the console at run time.

input('Greetings! Hopefully you are doing good Buddy. Press enter to continue.')

input("I'm a built-in scripted bot. My job is to generate your Bio Data based on your inputs. Press enter to continue.")

input('Welcome to our Bio Data Generator! Press enter to continue.')

studentName = input('Please enter your name here: ')
studentAge = int(input('Please enter your age here: '))

studentUniversityName = input('Please enter your university name here: ')
studentRollNo = int(input('Please enter your roll no here: '))
studentTechnology = input('Please enter your technology name here: ')
studentSection = input('Please enter your section here: ')

input("Now you don't have to write all your subjects name, our smartly written script will automatically generate a list and you can proceed without any delay. Press enter to continue.")

subjects = ['Python', 'ICT', 'English', 'Calculus', 'Physics']

questionAboutWebDevelopment = input('Say yes if you are interested in Web Development and our smart script will automatically generate a list of all latest tech languages and frameworks so, that you can just pick up all the ones you have a command over and simply add them to your Bio Data.')

languages = [
    'HTML5', 'CSS3', 'Bootstrap', 'JavaScript', 'React.js', 'Python', 
    'C', 'C++', 'C#', 'Java', 'React Native', 'Swift', 'Kotlin', 'MySQL', 
    'PHP', 'OOP'
]

selected_languages = []

print('Here is the list of available languages and frameworks:')

for i, language in enumerate(languages, 1):
    print(f'{i}. {language}')

while True:
    
    choice = input('Enter the number of the language you want to add to your bio, or type "exit" to finish: ')
    
    if choice.lower() == 'exit':
        break
    
    elif choice.isdigit() and 1 <= int(choice) <= len(languages):
        selected_languages.append(languages[int(choice) - 1])
    
    else:
        print('Invalid input. Please enter a valid number or "exit".')

input('Please fill all the correct matriculation credentials. Press enter to continue.')

studentMatriculationTotalMarks = int(input('Please enter your total marks of matriculation board here: '))
studentMatriculationObtainedMarks = int(input('Please enter your obtained marks of matriculation board here: '))

input('Please fill all the correct intermediate credentials. Press enter to continue.')

studentIntermediateTotalMarks = int(input('Please enter your total marks of intermediate board here: '))
studentIntermediateObtainedMarks = int(input('Please enter your obtained marks of intermediate board here: '))

input('Our smart script will automatically calculate your both matric and intermediate percentages so, you don’t have to worry at all. Press enter to continue.')

# Calculating Matriculation percentage
studentMatriculationPercentage = studentMatriculationObtainedMarks / studentMatriculationTotalMarks * 100

# Calculating Intermediate percentage
studentIntermediatePercentage = studentIntermediateObtainedMarks / studentIntermediateTotalMarks * 100

input('Grades will automatically be detected based on your matric and intermediate percentages. Press enter to continue.')

# Determining the grades
def determine_grade(percentage):
    if 80 <= percentage <= 100:
        return 'A+'
    elif 70 <= percentage < 80:
        return 'A'
    elif 60 <= percentage < 70:
        return 'B'
    elif 50 <= percentage < 60:
        return 'C'
    elif 40 <= percentage < 50:
        return 'D'
    elif 30 <= percentage < 40:
        return 'E'
    elif 20 <= percentage < 30:
        return 'F'
    elif 10 <= percentage < 20:
        return 'G'
    else:
        return 'Fail'

studentMatriculationGrade = determine_grade(studentMatriculationPercentage)
studentIntermediateGrade = determine_grade(studentIntermediatePercentage)

input('Loading...\n Your bio data is generated.\n Press enter to continue.')

# Printing the student bio data

print('BIO DATA')

print('According to your given information your bio data involves the following:')
print('Your name is', studentName)
print('Your age is', studentAge)
print('Your roll no is', studentRollNo)
print('Your technology is', studentTechnology)
print('Your section is', studentSection)
print('Your subjects of BSC Software Technology Are:')

for i, subject in enumerate(subjects, 1):
    print(f' {i}) {subject}')

print('Your selected tech languages are:')

for i, language in enumerate(selected_languages, 1):
    print(f' {i}. {language}')

print(f'Your matriculation percentage is {studentMatriculationPercentage:.2f}%')
print(f'Your intermediate percentage is {studentIntermediatePercentage:.2f}%')
print('Your matriculation grade is', studentMatriculationGrade)
print('Your intermediate grade is', studentIntermediateGrade)

print('The process of generating your Bio Data has been completed successfully!')