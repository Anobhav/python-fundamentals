class calculator:
    def __init__(self,n):
        self.n=n
    
    def square(self):
        print(f"sqaure of {self.n} is {self.n*self.n}")

    def cube(self):
        print(f"cube of {self.n} is {self.n*self.n*self.n}")
    
    @staticmethod
    def greet():
        print("hello")

a=calculator(5)
a.square()
a.cube()
