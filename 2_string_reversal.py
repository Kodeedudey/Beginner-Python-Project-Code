#String Reversal Program

st=input("Enter the string  ")


#Method 1
st1=""
for i in st:
    st1=i+st1
print("\nMethod1")
print("\nThe reversed string is:",st1)


#Method 2
print("\nMethod 2")
print("\nThe strin is: ",st[::-1])
