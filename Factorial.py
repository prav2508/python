n = int(input("Enter the number to find its factorial!"))
def factorial(n):
    fact = 1
    for i in range(1,n+1,1):
        fact = fact*i
    return fact
def facto(n):
    if n == 0:
        return 1
    else:
        return n*facto(n-1)
numb = factorial(n)
x = facto(n)
print(numb,x)
