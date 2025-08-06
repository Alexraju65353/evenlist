m = int(input("Enter the starting number,m:"))
n = int(input("Enter the ending number,n:"))
squaresset = {x**2 for x in range (m,n+1) if x % 2 == 0}
print("Set of squares of even numbers between {m} and {n}:")
print(squaresset)
