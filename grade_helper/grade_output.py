def print_status(name,grade):
    
    if grade >=90:
       print(name,grade,"excellent!")
    elif 60<=grade<90:
        print(name,grade,"passed!")
    else:
        print(name,grade,"failed!")
    
    return grade
    