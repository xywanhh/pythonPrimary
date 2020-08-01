from math import pi

class Circl:
    def __init__(self, r):
        self.r = r
    def area(self):
        return pi * self.r * self.r
    def premeter(self):
        return 2 * pi * self.r

class Ring:
    def __init__(self, r1, r2):
        self.c1 = Circl(r1)
        self.c2 = Circl(r2)
    def area(self):
        return self.c1.area() - self.c2.area()
    def premeter(self):
        return self.c1.premeter() - self.c2.premeter()

if __name__ == '__main__':
    c1 = Circl(10)
    print(c1.area())
    print(c1.premeter())

    c2 = Ring(10, 3)
    print(c2.area())
    print(c2.premeter())