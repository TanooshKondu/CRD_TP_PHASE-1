#instance level var (static level programming)
#static level var 
#local level var

class A:
    abc =10
    def fun1(self):
        a =9
        self.b = 0 
        print(self.abc)
o=A()
o.fun1()