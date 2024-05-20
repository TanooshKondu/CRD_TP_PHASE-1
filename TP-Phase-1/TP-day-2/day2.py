#<----------------functions------------>

def cr(x:int, y:int)-> int:
    return x+y
a=int(input())
b = int(input())
print(cr(a,b))

def cr(a:int, b:int) -> int:
    print(a+b)
a='8'
b='9'
print(cr(a,b))

#<--------------------default argument---------------->
def cr(a,b=0):
    print(a,b)
cr(4,6)
#<-----------------keyword arg--------------->
def cr(a,b=0):
    print(a,b)
cr(b=4,a=6)
#<----------------variable number of arg-------------------->
def cr(a,*b):
    print(a,b)
cr(6,9,0,8,9,8) #cr(6,9,0,8,9, a=8)

#<------------lambda fun------------>
c= lambda a,b: a+b
print(c(5,5))

#<-----------for loop------->
s=input()
##for var in collection
for i in s:
    print(i)
for i in range(len(s)):
    print(i, s[i])
#<----slicing--->
s="dshyugalfiuhsqeiuhfio"
print(s[1:7:3], s[:7:], s[::-1])

###<<<----------methods------------>>>
s="hgf hGF abdh"
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())
#.is*** gives boolean values
print(s.istitle())
print(s.isupper())
print(s.islower())
#<-----index--->
print(s.index('h',3,8))
print(s.count('h'))
print(s.rindex('h'))
print(s.find('z'))

print(s.startswith('ab', 8))#boolean

###<<--- Split fun --->>
s="hgf hGF abdh"
print(s.split())#list
print(s.split('h', maxsplit = 1))#list
print(s.partition('h'))#tuple

##<<-----formatting---->>
a=8
b=7
print(f"addition of {a} and {b} is {a+b}")
print("addition of {0} and {2} is {1}".format(a,a+b,b))