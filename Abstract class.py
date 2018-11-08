from abc import ABC,abstractmethod  # import abc module for abstract base class
class a(ABC):   # inherits ABC class
    @abstractmethod  #decorator to indicate abstarct method
    def foo(self):
        pass
class b(a):

    def foo(self):
        print("inside b class")
class c(a):
    def foo(self):
        print("inside c class")
a = b()  #cannot intantiate class a because its absract class
a.foo()
