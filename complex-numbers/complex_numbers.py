"""
Set task: Implement complex numbers.
Method: Implement the simple mathematical processes to compute complex numbers.
Example: None
"""

from math import sqrt, e, cos, sin


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        if self.imaginary < 0:
            return f"{self.real}{self.imaginary}*i"
        return f"{self.real}+{self.imaginary}*i"

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        if type(other) == ComplexNumber:
            return ComplexNumber(
                self.real + other.real,
                self.imaginary + other.imaginary
            )
        else:
            return ComplexNumber(
                self.real + other,
                self.imaginary
            )

    def __mul__(self, other):
        if type(other) == ComplexNumber:
            return ComplexNumber(
                self.real * other.real - self.imaginary * other.imaginary,
                self.real * other.imaginary + self.imaginary * other.real
            )
        else:
            return ComplexNumber(
                self.real * other,
                self.imaginary * other
            )

    def __sub__(self, other):
        if type(other) == ComplexNumber:
            return ComplexNumber(
                self.real - other.real,
                self.imaginary - other.imaginary
            )
        else:
            return ComplexNumber(
                self.real - other,
                self.imaginary
            )

    def __truediv__(self, other):
        if type(other) == ComplexNumber:
            return ComplexNumber(
                (self.real * other.real + self.imaginary * other.imaginary) / (other.real ** 2 + other.imaginary ** 2),
                (self.imaginary * other.real - self.real * other.imaginary) / (other.real ** 2 + other.imaginary ** 2)
            )
        else:
            return ComplexNumber(
                self.real / other,
                self.imaginary / other
            )

    def __abs__(self):
        return sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(
            self.real,
            -1 * self.imaginary
        )

    def exp(self):
        return ComplexNumber(
            e ** self.real * cos(self.imaginary),
            e ** self.real * sin(self.imaginary)
        )
