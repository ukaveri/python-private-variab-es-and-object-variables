'''
class Person:
    def input1(self,fname,age):
        self.name = fname
        self.a = age
    def display(self):
        print(self.name,",",self.a)
#here fname and age are the local members of input1 method
#but name and a are the object members 
ram=Person()
ram.input1('krishn',20)
ram.display()
sita=Person()
sita.input1('radha',25)
sita.display()
ram.fname='radha'
ram.display()
sita.fname = 'krishn'
sita.display()
we get error because there is difference in local members and
object members.
'''
#write a program to demonstrate private data members
#we give private data members by self.__variable
'''
class Person:
    def input1(self,fname,age):
        self.__fname=fname
        self.__age = age
    def input2(self,iname):
        self.__iname = iname
    def display(self):
        print(self.__fname,",",self.__age,",",self.__iname)
ram = Person()
ram.input1("krishn",20)
ram.input2("madhav")
ram.display()
sam = Person()
sam.input1("Radha",25)
sam.input2("Madhavi")
sam.display()
ram.__fname = "khanna"
sam.__iname = "kishori"
#..................................................................
#here underscore is present in main method which means outside the
#class so here the class is public not private but the 2underscosres
#represent the private.
#..................................................................
ram.display()
sam.display()
'''
