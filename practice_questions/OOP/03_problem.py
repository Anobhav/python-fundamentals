# create a class 2 vector and use it to create another class reporesenting 3D vector 

class two_dim_vector:
    x=0,y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def show(self):
        print(f"x: {self.x} y: {self.y}")

class three_dim_vector(two_dim_vector):
    z=0

    def __init__(self, x, y,z):
        super().__init__(x, y)
        self.z=z

    def show(self):
        print(f"x: {self.x} y: {self.y} z: {self.z}")


a=two_dim_vector(5,10)
a.show()

b=three_dim_vector(5,10,15)
b.show