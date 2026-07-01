from grade_validation import validation_type, validation_name, validation_range_grade, validation_type_grade
from grade_data import students
from grade_output import print_status
from grade_logic import calc_average , print_passed_grade

def run_grade_helper():
    
    valid_grade_list=[] 
    
    for i in students:
        
        if validation_type(i):
            if validation_name(i[0]):
                if validation_type_grade(i[1]):
                    if validation_range_grade(i[1]):
                        valid_grade=print_status(i[0],i[1])
                        valid_grade_list.append(valid_grade)
    calc_average(valid_grade_list)
    print_passed_grade(valid_grade_list)
    
