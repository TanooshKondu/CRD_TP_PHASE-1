#pip install turtle
#pip install pyastro
#sets-------------->>>>
# s={7,0,9,5,0}
# print(s)

# a={8,0,5,9}
# b={0,7,3,2}
# print(a.union(b),a,b)
# print(a|b,a,b)
# print(a.update(b),a,b)
# print(a.difference(b),a,b)
# print(a-b,a,b)
# print(a.difference_update(b),a,b)


b= {0,8,9,5}
a={10,50,6,2}

print(a.intersection(b),a,b)
print(a&b,a,b)
print(a.intersection_update(b),a,b)


a={8,0,5,9}
b={0,7,3,2}
print(a.symmetric_difference(b),a,b)
print(a^b,a,b)
print(a.symmetric_difference_update(b),a,b)

a={8,0,5,9,7}
b={0,7}

print(a.issubset(b),a<b,a<=b)
print(a.issuperset(b),a>b,b>=b)