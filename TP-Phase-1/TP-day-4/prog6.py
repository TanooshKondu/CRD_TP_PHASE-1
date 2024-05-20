#using key values
n=int(input())
d={}
for i in range(n):
    key,val = map(int,input().split())
    d[key]=val
print(d)