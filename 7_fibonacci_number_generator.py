n=int(input("Enter fibnocci terms"))

a=0
b=1
count=0

if n<=0:
    print("Term entered is invalid\n")
elif n==1:
    print("\nThe fibonacci sequence is: ")
    print(a)
else:
    print("\nFibonacci Sequence is: \n")
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count=count+1
