def add(x,y):
    return (x+y)

def subtract(x,y):
    return (x-y)

def multiply(x,y):
    return(x*y)

def divide(x,y):
    return(x/y)


print("Welcome to the simple Arithmatic Calculator\n")
print("Select the operation\n")
print("1. Addition\n")
print("2. Subtraction\n")
print("3. Multiplication\n")
print("4. Division\n")


while True:
    x=int(input("Enter your choice in numerical value"))
    if x in (1,2,3,4):
        a=float(input("Enter first number: "))
        b=float(input("Enter second number: "))

        if x==1:
            print(a,"+",b,"=",add(a,b))
        elif x==2:
            print(a,"-",b,"=",subtract(a,b))
        elif x==3:
            print(a,"*",b,"=",multiply(a,b))
        else:
            print(a,"/",b,"=",divide(a,b))
    else:
        print("Invalid Input")

        
