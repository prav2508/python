class a:
    def show(self):
        print("inside class a")
class b:
    def show(self):
        print("inside class b ")
class c(a,b):
    def show(self):
        print("inside class c")
    def access(self):
        super().show()  # according to method resolution order the preference is from left to right,so show method of class a is executed. 

a = c()
a.show()
a.access()