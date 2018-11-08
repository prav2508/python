## use any one method to check the armstrong number


num = input("enter a number to check if its armstrong number")
intnum= int(num)


def method1(num):
    r=0
    for i in range(0, num.__len__(), 1):
        r += pow(int(num[i]), 3)
    if r == int(num):
        print("its armstrong number")
    else:
        print("not a armstrong number")
def method2(a):
    sum = 0
    for i in range(3):
        n = a % 10
        a = int(a / 10)
        sum = (sum + (n * n * n))

    if intnum == sum:
        print("its armstrong number")
    else:
        print("not a armstrong number")

#method1(num)
method2(intnum)