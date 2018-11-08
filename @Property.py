class person:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    @property   #this property decorator is used to use that email method as an attribute(acts as a getter)
    def email(self):
        return self.first+"_"+self.last+"@gmail.com"
    @property   #this property decorator is used to use that fullname method as an attribute(acts as a getter)
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    @fullname.setter  #this property decorator is used to use that function method as an attribute to set values(acts as a setter)
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter  #this property decorator is used to use that function method as an attribute to delete values(acts as a deleter)
    def fullname(self):
        self.first = None
        self.last = None
        print("deleted")
obj = person("james","bond")

obj.fullname="praveen p"

print(obj.first)
print(obj.fullname)
print(obj.email)

del obj.fullname   # to delete the the values

