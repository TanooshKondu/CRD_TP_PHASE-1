####multiple inheritance
class A:
    def fun1(self):
        print("fun1-A")
    def fun2(self):
        print("fun2-A")
class B:
    def fun1(self):
        print("fun1-B")
    def fun2(self):
        print("fun2-B")
class C(A,B):
    def fun3(self):
        print("fun3")
    def fun4(self):
        print("fun4")
o = C()
o.fun2()