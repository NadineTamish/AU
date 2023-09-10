""" Module for complex numbers calculations """


class ComplexNumbers:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary < 0:
            return f'{self.real:.2f} {self.imaginary:.2f} i'
        return f'{self.real:.2f} + {self.imaginary:.2f} i'

    def __add__(self, other):
        return ComplexNumbers((self.real + other.real),
                              (self.imaginary+other.imaginary))

    def __sub__(self, other):
        return ComplexNumbers((self.real - other.real),
                              (self.imaginary - other.imaginary))

    def __mul__(self, other):
        return ComplexNumbers(
            self.real*other.real-self.imaginary*other.imaginary,
            self.imaginary*other.real+self.real*other.imaginary)

    def __truediv__(self, other):
        return ComplexNumbers(
            (self.real*other.real+self.imaginary*other.imaginary)/(other.real**2+other.imaginary**2)
            , (self.imaginary*other.real-self.real*other.imaginary)/(other.imaginary**2+other.real**2))

    def modulus(self):
        return round((self.real**2+self.imaginary**2)**0.5, 2)


C = ComplexNumbers(3, 2)
D = ComplexNumbers(-4, -5)
print(C+D)
print(C-D)
print(C*D)
print(C/D)
print(C.modulus())
print(D.modulus())
