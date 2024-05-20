#single, double linked lists

class node:
    def __init__(self,data):
        self.data=data
        self.next = None
        
o= node(1)
o1=node(2)
o2=node(3)
o.next=o1
o1.next = o2



##infosys ques!!

class ClassA:
    def first_method(self):
        print("Johnny Johnny...")
    def second_method(self):
        print("Yes Papa...")
    def third_method(self):
        print("Eating Sugar...")
class ClassB(ClassA):
    def second_method(self):
        super().first_method()
        super().second_method()
        super().third_method()
        print("No Papa...")
    def third_method(self):
        print("Telling Lies..")
class ClassC(ClassB):
    def first_method(self):
        print("Open Your mouth... Ha..Ha..Ha..")
    def second_method(self):
        print("No Papa...")
    def third_method(self):
        super().first_method()
        super().second_method()
        super().third_method()
obj_A = ClassA()
obj_B = ClassB()
obj_C = ClassC()