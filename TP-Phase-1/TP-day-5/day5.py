class student:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def printing(self):
        print(self.a, self.b)
s1 = student(2,3)
s1.printing()

######33
##<<<<------Polymorphysim ----------->>>>
class student:

    def __init__(self,a,b):
        print("sdjknfljke")
    def printing(self):
        print("kljsdf")
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def printing(self):
        print(self.a,self.b)### polymorphysim
s1 = student(2,3)
s1.printing()
