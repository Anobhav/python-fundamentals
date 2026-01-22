class Programmer:
    company = "Microsoft"

    def __init__(self, name, language):
        self.name = name
        self.language = language
    
    def getinfo(self):
        print(
            f"Name is {self.name}, "
            f"language is {self.language}, "
            f"company is {self.company}"
        )

a = Programmer("Anobhav", "Python")
a.getinfo()

b = Programmer("Harry", "C++")
b.getinfo()
