m=int(input("enter the starting number:"))
n=int(input("enter the ending number:"))
even_squares = sorted({x**2 for x in range(m,n+1) if x%2==0})
print("set of squares of even no's:",even_squares)
