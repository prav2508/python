# single level inheritance
class a:  #superclass
    def show1(self):
        print("hello")
class b(a):  #subclass
    def show2(self):
        print("hi")

#multi level inheritance
class c(b):
    def show3(self):
        print("buddy")

#multiple inheritance
class d:
    def xyz(self):
        print("from class d")
class e(a,d):
    pass

obj = b()  # now obj inherits from class a features as well as class b features
obj1 = c()
obj2 = e()
obj.show1()
obj.show2()
obj1.show3()
obj1.show1()
obj1.show2()
obj2.xyz()
obj2.show1()