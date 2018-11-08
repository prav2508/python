class Student:
    def __init__(self,m1,m2):
       self.m1 = m1
       self.m2 = m2

    def __add__(self, other):   #overloaded method to add 2 objects
        s1 = self.m1 + other.m1
        s2 = self.m2 + other.m2
        s3 = Student(s1,s2)
        return s3
    def __str__(self):   #overloaded method of print method
       return "[m1={},m2={}]".format(self.m1,self.m2)
s1 = Student(77,89)
s2 = Student(74,99)
s3 = s1 + s2
print("s3 marks are {},{}".format(s3.m1,s3.m2))
print("---------------------------")
print(s3)  #it calls __str__() method behind the scene, so to print the object value we need to overload it..
print("---------------------------")