l= [3,6,9,0,"gfdg",True]
print(*l)
l = input().split()
print(l,type(l))#excepting str list from user

#str list to int
l=input().split()
for i in range(len(l)):
    l[i] = int(l[i])
print(l,type(l))

l =[int(i) for i in input().split()]
print(l,type(l))

#map func
l = list(map(int,input().split()))
print(l,type(l))
#lambda
l=[3,4,5,6,7,8,0]
l=list(map(lambda x:x*x,l))
print(l)
#filter
l=[3,4,5,6,7,8,0]
l=list(filter(lambda x:x%2==0,l))
print(l)
#append vs extend
l=[3,4,5,6,7,8,0]
print(l.append("abcd"))
print(l.extend("abcd"))
print(l.insert(0,9))

#pop,clear,del
l=[3,4,5,6,7,8,0]
l.pop()
print(l)
l.pop(0)
print(l)
l.remove(0)
print(l)
l.clear()
print(l)
#SORT, sorted
l=[3,4,5,6,7,8,0]
l.sort(reverse=True)
print(l)
print(sorted(l),l)
#sorted elements
l=['hfh','dfgh',"fghj","gh","trdhu"]
l.sort(key=len)
print(l)
a=[[5,6],[0,9,8],[3,6,5],[0,0]]
print(sorted(a,key=sum))
print(sorted(a,key=lambda x:x[1]))
#repetation
a=[0,9,8]
l=[0]*5
print(a+[0,9],a*4)


##<<<------tuples----->>>
t=(6,7,8,0,5,3)
t=tuple(map(int,input().split()))
print(t,type(t))