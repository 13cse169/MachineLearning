class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)

class Child(Person):
    pass

c1 = Child("Birendra", "Singh")

c1.printname()

