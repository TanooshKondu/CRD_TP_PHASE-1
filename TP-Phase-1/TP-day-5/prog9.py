class A:
    def __init__(self):
        print("A")
    def _fun(self):
        print("_fun")
class B(A):
    def __init__(self):
        print("B")
    def _fun1(self):
        print("_fun1")
a=A()
b=B()