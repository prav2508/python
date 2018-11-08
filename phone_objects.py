class phone:
    def __init__(self, ram, brand, cost): #somthing like a constructor in java
        self.ram = ram
        self.brand = brand
        self.cost = cost

    def config(self):  #these functions are called as method in oops
        print("the config is: ram={},brand={},cost={}".format(self.ram,self.brand,self.cost))
    def compare(self,others):
        if self.brand == others.brand:
            return True
        else:
            return False
obj1 = phone(2,"Mi",6000)           # objects are created with constructors to initialize
obj2 = phone(6,"oneplusone",37000)

obj1.config()  #calling the methods using objects
obj2.config()

if obj1.compare(obj2):
    print("its same")
else:
    print("its different")