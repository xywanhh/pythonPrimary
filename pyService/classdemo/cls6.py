class A:
    def hahaha(self):
        print('A')

class B(A):
    def hahaha(self):
        super().hahaha()
        #super(B,self).hahaha()
        #A.hahaha(self)
        print('B')
    def f1(self):
        a = A()
        A.hahaha(a)
        self.hahaha()

    def f2(self):
        A.hahaha(self)

a = A()
b = B()
b.hahaha()
super(B,b).hahaha()
b.f1()
