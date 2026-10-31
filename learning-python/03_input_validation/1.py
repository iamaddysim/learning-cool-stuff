# Recursion Function
def show(n):
    if(n == 0):
        return
    print(n, end=" ")
    show(n-1)

m = int(input("Enter a number:"))
show(m)