def add(x,y):
    return x+y
print(add(2,3))  # position argument type of calling the function
print("------------")
def add1(name,age):
    print(name)
    print(age)
add1(name="praveen",age="22") # keyword arguement type of calling the function
print("------------")
def add2(name,age=18):
    print(name)
    print(age)
add2(name="praveen") # default arguement type of calling the function
print("------------")
def add3(*y):  # it takes the arguements in the form of tuple dynamically
    c = 0
    for i in y:
        c = c + i
    return c
print(add3(2,3,4,99))  # variable length argument type of calling the function
print("------------")
def add4(**kwargs): # it takes the arguments as key value pair dynamically
   print(kwargs)
   for i,j in kwargs.items():
       print(i,j)
add4(name="praveen",age=22) # keyword variable length arguement type of calling the function
print("------------")