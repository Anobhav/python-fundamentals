class anobhav:
    # below are class attributes 
    name= "anobhav"
    language="Py"
    def __init__(self,age=0): # this is a dunder method, they always start with _ _ 
        print("I am creating a object")
        self.age=age

    def getinfo(self):
        print(f"language{self.language}, name: {self.name}, age: {self.age}")


a=anobhav()
a.getinfo()
b=anobhav()
b.age=22 # this is a object/instance attribute
print(b.name, b.language, b.age)