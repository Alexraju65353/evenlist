l1=[]
l2=[]
a=int(input("enter the range:"))
for i in range (a):
    x=int(input("Enter the elememts of the list:"))
    l1.append(x)
print("The list:",l1)    
for i in l1:
    if i not in l2:
        l2.append(i)

print("The new list is",l2)        
