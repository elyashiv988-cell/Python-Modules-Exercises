def calc_average(grade_list):
    
    try:
        print(f"the averege is {sum(grade_list)/len(grade_list)}")
    except ZeroDivisionError:
        print("there isn't any grades")
    
def print_passed_grade(list):
    i=0
    for _ in list:
        if _ >=60:
            i+=1
    print("Passed students:",i)
