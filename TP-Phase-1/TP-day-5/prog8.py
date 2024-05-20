class A:
    def fun1(self):
        pass
    def fun2(self):
        pass
class B():
    def fun3(self):
        pass
class C():
    def fun4(self):
        pass
class D(A,C):
    pass
a=A()
b=B()
c=C()
d=D()