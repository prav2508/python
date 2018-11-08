from functools import *
num = [2,4,5,9,7,8,6,3,1]

x = list(filter(lambda a: a % 2 != 0, num))
print("even numbers are: {}".format(x))

y = list(map(lambda a: pow(a, 2), x))
print("square of even numbers: {}".format(y))

sum = reduce(lambda n, m: n+m,y)
print("The sum of square of even numbers is: {}".format(sum))