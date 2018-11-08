class laptop:
    def code(self,ide):
        ide.execute() #expecting execute method in ide type object
class pycharm:
    def execute(self):  # must contain execute method
        print("coding and compiling!! (from pycharm)")
class atom:
    def execute(self):   # must contain execute method
        print("coding,compiling,spell check,results,etc  (from atom)")

#can use either of ide pycharm or atom

i = atom()
#i = pycharm()


obj = laptop()
obj.code(i) # the ide argument will accept an object of type pycharm or atom (loose coupling) ,provided the object type has execute method
