



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
               