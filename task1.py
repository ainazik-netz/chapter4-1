class Student:
    def __init__(self,name,lastname,department,year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance
get_student_info = Student('Mary','Black', 
'software engineering','2019')
print(get_student_info.name +' '+ get_student_info.lastname +' '+ 
'entered the department' +' '+ get_student_info.department + ' ' +
'of the NYU in  year' + get_student_info.year_of_entrance)
#  print(get_student_info.name,get_student_info.lastname
#  'entered the department', get_student_info.department
#  'of the NYU in  year',get_student_info.year_of_entrance)