
students = [("Dana", 82),("Tom", 55),("Maya", 91),("Ron", 60),("Noa", "88"),("Ben", 120),("Lior", -5),(55, 70),["bob",5]]


def validation_type(data):
    if type(data)==tuple:
        return True
    else:
        print("invalid data")

def validation_name(name):            
    if type(name)==str:
        return True
    else:
        print("invalid name")    

def validation_grade(grade):
    if type(grade)==int and 0<grade<101:
        return True
    else:
        print("invalid grade")
               
            

def print_status(name,grade):
    
    if grade >=90:
       print(name,grade,"excellent!")
    elif 60<=grade<90:
        print(name,grade,"passed!")
    else:
        print(name,grade,"failed!")
    
    return grade
    
  

def calc_average(grade_list):
    
    try:
        print(f"the averege is {sum(grade_list)/len(grade_list)}")
    except ZeroDivisionError:
        print("there isn't any grades")


def main():
    
    passed_grades=[] 
    for i in students:
        
        if validation_type(i):
            if validation_name(i[0]):
                if validation_grade(i[1]):  
                    grade=print_status(i[0],i[1])
                    passed_grades.append(grade)

                    
    calc_average(passed_grades)

main()      

