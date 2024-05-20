from dataclasses import dataclass
@dataclass()
class x:
    a:int
    b:str
    c:int
#o=x(1,"abc",8)
o=x("abc","abc",8)
print(o.a,o.b,o.c)