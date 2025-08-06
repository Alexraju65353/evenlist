ls=[]
num=int(input("Enter the number of tuples:"))
for i in range (num):
    x1=int(input("Enter the 1st element of the tuple:"))
    x2=int(input("enter the 2nd element of the tuple:"))
    ls.append((x1,x2))
#l=len(ls)    
for i in range(num):
    for j in range(0,num-i-1,):
        if (ls[j][1]>ls[j+1][1]):
            temp=ls[j]
            ls[j]=ls[j+1]
            ls[j+1]=temp
print("sorted list:",ls)            



