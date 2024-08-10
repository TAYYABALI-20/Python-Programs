# Calculate student percentage using function on runtime by taking user input

sub_total_marks = int(input('Enter your total subject marks here: '))

sub_marks_1 = int(input('Enter your Python subject marks out of (50) here: '))
sub_marks_2 = int(input('Enter your ICT subject marks out of (50) here: '))
sub_marks_3 = int(input('Enter your Islamiat subject marks out of (50) here: '))
sub_marks_4 = int(input('Enter your English subject marks out of (50) here: '))
sub_marks_5 = int(input('Enter your Math subject marks out of (50) here: '))
sub_marks_6 = int(input('Enter your Physics subject marks out of (50) here: '))

def student_marks(sub1, sub2, sub3, sub4, sub5, sub6):
    
    return sub1 + sub2 + sub3 + sub4 + sub5 + sub6

def student_percentage():
    
    total_marks = sub_total_marks
    
    obtained_marks = student_marks(sub_marks_1, sub_marks_2, sub_marks_3, sub_marks_4, sub_marks_5, sub_marks_6)
    
    percentage = (obtained_marks * 100) / total_marks
    
    print(f'\nYour percentage = {percentage:.2f}')

student_percentage()