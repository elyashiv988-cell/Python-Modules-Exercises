from grade_helper.grade_validation import validation_type, validation_name, validation_grade
from grade_helper.grade_data import students
from grade_helper.grade_output import print_status
from grade_helper.grade_logic import calc_average

def run_grade_helper():
    valid_grade_list=[] 
    
    for i in students:
        
        if validation_type(i):
            if validation_name(i[0]):
                if validation_grade(i[1]):  
                    valid_grade=print_status(i[0],i[1])
                    valid_grade_list.append(valid_grade)

                    
    calc_average(valid_grade_list)
