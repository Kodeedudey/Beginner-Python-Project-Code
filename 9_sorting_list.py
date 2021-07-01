n=int(input("Enter th e size of the list"))

lt=[]
print("Enter the list items: \n")

for i in range(0,n):
    p=int(input())
    lt.append(p)

print("The entered list is: ",lt)



#sorting the list
for i in range(0,len(lt)):
    for j in range(0,len(lt)-1):
        if(lt[j]>lt[j+1]):
            temp=lt[j]
            lt[j]=lt[j+1]
            lt[j+1]=temp

print("\nThe reversed list is: ",lt)
    

