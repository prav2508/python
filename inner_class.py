class Person:
    def __init__(self,name,age,phone):
        self.name = name
        self.age = age
        self.Phone=phone #to initialize inner class object
    class Phone:
        def __init__(self,brand,cost):
            self.brand = brand
            self.cost = cost

    def show(self):
        print("person:[name={},age={},phone={},{}]".format(self.name,self.age,self.Phone.brand,self.Phone.cost))


p1 = Person.Phone("mi",6000)
p2 = Person.Phone("samsung",8000)

obj1 = Person("praveen",22,p1)
obj2 = Person("ravi",30,p2)

obj1.show()
obj2.show()
print(obj1.Phone.brand)    #to access inner class variable