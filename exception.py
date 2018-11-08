a = 5
#b = "p"
b = 0
try:
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print("cannot divide by zero =[{}]".format(e))
except Exception as e1:
    print(e1)