#Program to process User Record
d=dict()
n=int(input("How many students' record you want to store"))

for i in range(0,n):
    a,b=input("Enter the first and last name of the student").split()
    c=input("Cntanct Number")
    m=input("Enter avg marks: ")
    d[a,b]=(c,m)


def maxmarks():
    l=list()
    for name,detail in d.items():
        l.append(detail[1])
    l=sorted(l)
    print("Maximum marks:",max(l))
    return

def searchdetail(fname):
    ls = list()
     
    for sname,details in d.items():
       
        tup=(sname,details)
        ls.append(tup)
         
    for i in ls:
        if i[0][0] == fname:
            print(i[1][0])
    return

def options():
    j=int(input("""Enter your choice\n
                1. To find maximum marks\n
                2. Search contact using First name\n
                3. Exit\n
                """))
    if(j==1):
        maxmarks()
        print("Want to execute any other operation? y/n:")
        i=input()
        if(i=='y'):
            options()
        else:
            exit()
    elif(j==2):
        searchdetail(input("Enter the first name of student: "))
        print("Want to execute any other operation? y/n:")
        i=input()
        if(i=='y'):
            options()
        else:
            exit()
    else:
        print("Thanks for executing the program!")
        return

options()
        
            
    


