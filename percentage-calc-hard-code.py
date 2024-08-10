# Calculate student percentage using function
def student_marks(sub1, sub2, sub3, sub4, sub5, sub6):
    
    return sub1 + sub2 + sub3 + sub4 + sub5 + sub6

def student_percentage():
    
    total_marks = 300
    
    obtained_marks = student_marks(45, 41, 46, 35, 30, 48)
    
    percentage = (obtained_marks * 100) / total_marks
    
    print(f'Your percentage = {percentage:.2f}')

student_percentage()