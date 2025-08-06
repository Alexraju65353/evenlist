string=input("enter the string:")
l1=list(string)
l2=[]
for i in range(len(l1)):
    if l1[i] not in l2:
        l2.append(l1[i])
print(l2)          