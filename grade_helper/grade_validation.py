def validation_type(data):
    if type(data)==tuple:
        return True
    else:
        print("Data must be a tuple")

def validation_name(name):            
    if type(name)==str:
        return True
    else:
        print("Skipped student: Name must be a string")    

def validation_type_grade(grade):
    if type(grade)==int:
        return True
    else:
        print("Skipped student: Grade must be an integer")
def validation_range_grade(grade):
    if 0<grade<101:
        return True
    else:
        print("Skipped student: Grade must be between 0 and 100")
    
    