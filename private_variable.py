class A:
    def __init__(self,var):
        self.__test = var  # private original variable
    def get_var(self):
        return self.__test
a=A(10)

#print(a.__test)  # this line must throw error,because this variable is private nad can be accessed by methods only !!
print(a.get_var())