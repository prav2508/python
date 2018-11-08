class Person:
    creature = "human"  #class variable

    def __init__(self,name,age):  #name,age are instance variables
        self.name = name
        self.age = age
    def get_name(self):   #accessors (instance methods)
        return self.name
    def set_name(self, name):#mutators (instance methods)
        self.name=name

    @classmethod  #decorators to treat this method as class method
    def get_creature(cls):  #class method
        return cls.creature
    @staticmethod  #decorators to treat this method as static method
    def info():  #static method
        print("inside static method")
ref1 = Person("praveen",22)
ref2 = Person("ravi",30)

print(ref1.get_name())  #calling instance method
print(ref2.get_name())  #calling instance method

print(Person.get_creature()) #calling class method
print(Person.info())  #calling static method