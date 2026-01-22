class Employee:
    company="ABC"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self):
        print(f"name of employee: {self.name} and salary is {self.salary}")
    

class programmer(Employee):
    company="ABC TECH"
    def __init__(self, name, salary,language):
        super().__init__(name, salary)
        self.language=language
    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")


a=Employee("Harry", "1")
b=programmer("Anobhav","1","py")

print(a.company, b.company)

b.show()
b.show()

# inheritance is of 4 types 