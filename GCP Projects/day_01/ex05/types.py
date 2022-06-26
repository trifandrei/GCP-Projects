def convert(list):
    return tuple(i for i in list)

def convert_tolist(line):
        f_list=[]
        list=line.split(",")
        for l in list:
            if '\n' not in l:
                f_list.append(int(l))
            else:
                a=l.split(" \n")
                f_list.append(int(a[0]))
        return f_list

def create_dection(line):
        line.sort()
        list=[]
        length=int(len(line))

        for i in range(length):
            list.append(int(i))

        dictionary = dict(zip(list, line))
        return dictionary

def create_type():
    try:
        file1 = open('demo.txt', 'r')
    except FileNotFoundError:
        print("Invalid input")
    try:
        Lines = file1.readlines()
    except ValueError:
        print("Invalid input")
    
    count = 0
    f_list=[]
    tuple=()

    for line in Lines:

        f_list=convert_tolist(line)

        if count==0:
            print(f_list)

        if count==1:
           tuple=convert(f_list)
           print(tuple)

        if count==2:
           dict=create_dection(f_list)
           print(dict)
           
        count=count+1
      
           


create_type()