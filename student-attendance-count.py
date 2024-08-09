print('Welcome to our Python Student Attendence Calculator. \n')

studentName = str(input('Please enter your name here: '))

totalClasses = 30

classesAttended = int(input(f'\nDear {studentName}, how many classes do you have attended out of 30? '))

studentAttendencePercentage = (classesAttended * 100) / totalClasses

if studentAttendencePercentage >= 75:
    
    print(f'\nDear {studentName}, you have attended {classesAttended} out of {totalClasses}, and your attendance percentage is {studentAttendencePercentage: .2f}%.')
    
    print(f'\nDear {studentName}, you are allowed to sit in the exam.')
    
else:
    
    print(f'\nDear {studentName}, you have attended {classesAttended} out of {totalClasses}, and your attendance percentage is {studentAttendencePercentage: .2f}%.')
    
    print(f'\nDear {studentName}, you are not allowed to sit in the exam.')