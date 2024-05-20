def fun(a):
    a[0]=0
b=[1,2,3,4,5]
fun(b)
print(b)
######
a=[3,4,5,6]
b=a 
print(id(a), id(b))
b[0]=9
print(a,id(a),id(b))

###
d={6: 7, 8: 9, 0: 5}
print(d.keys())
print(d.values())
print(d.items())

#for loop in dict
d={6: 7, 8: 9, 0: 5}
for i in d:
    print(i, d[i])
for i,j in d.items():
    print(i,j)
##pop, get, setdefault
d={6: 7, 8: 9, 0: 5}
print(d.pop(0), d)
print(d.popitem(),d)
print(d.get(8), d)
print(d.setdefault(0),d)