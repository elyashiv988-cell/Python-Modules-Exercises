
students = [
    ("Dana", 82),
    ("Tom", 55),
    ("Maya", 91),
    ("Ron", 60),
    ("Noa", "88"),
    ("Ben", 120),
    ("Lior", -5),
    (55, 70),
    ["bob",5]]

valid_list=[]
def validation_data(all,name,grade):
    
    
    if type(all)==tuple and type(name)==str and type(grade)==int:
        
        valid_list.append(all)
    else:
        valid_list.append("invalid value")






def print_status(name,grade):
    
    
        if grade >=90:
            print(name,grade,"excellent!")
        elif 60<=grade<90:
            print(name,grade,"passed!")
        else:
            print(name,grade,"failed!")



def calc_average(averege):
    
    for i in valid_list:
        averege+=i[1]
    print(f"the averege is {averege/len(valid_list)}")


def main():
    while True:
        for i in students:
            validation_data(i,i[0],i[1])
        for i in valid_list:
            print_status(i[0],i[1])
        break
    calc_average(0)

main()



