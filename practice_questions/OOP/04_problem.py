# perform operator overloading

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def show(self):
        print(f"{self.real} + {self.imag}i")

c1 = Complex(1, 2)
c2 = Complex(3, 4)
c3 = Complex(-2, 1)
c4 = Complex(0, -3)

# Perform chained addition: (((c1 + c2) + c3) + c4)
result = c1 + c2 + c3 + c4
result.show()
