l1=[]
n=int(input("Enter th range of list"))
for i in range (n):
    x=int(input("enter the numbers"))
    l1.append(x)
print("the list is:",l1)
l2=[]
for i in l1:
    if i%2==0:
        l2.append(i)
print("even list:",l2)            