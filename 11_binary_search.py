n=int(input("Enter the list size"))
lst=[]
print("\nEnter items in sorted order: ")
for i in range(0,n):
    p=int(input())
    lst.append(p)

print("The list entered is: ",lst)

x=int(input("\n Enter the item you wnat to search: "))

end=len(lst)-1

front=0
mid=0

while end>=front:
    mid=(front+end)//2

    if(lst[mid]>x):
        end=mid-1
    elif (lst[mid]<x):
        front=mid+1
    else:
        print("\nElement fount ot the index: ",mid)
        break

else:
    print("\nElement not found")
