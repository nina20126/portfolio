'''
A complex number is a number that can be expressed in the form a + bi, where a and b are real numbers and i is the imaginary unit. 
Create class Complex with attributes, constructors and getters/setters.
'''
class Complex:

    type = 'i'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getComplex(self):
        complex_num = f"{self.a + self.b}{self.type}"
        return complex_num
    
    def get_a(self):
        return self.a
    
    def get_b(self):
        return self.b
    
    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

my_complex = Complex(3, 1.222222)
print(my_complex.getComplex())

my_complex.set_a(0.00004)
my_complex.set_b(999)
print(my_complex.getComplex())
my_complex.set_a(12.12)
print(my_complex.get_a())
print(my_complex.get_b())