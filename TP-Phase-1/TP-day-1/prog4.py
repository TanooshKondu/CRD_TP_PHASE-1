#take 2 nums from user and multiply them without using //, / % Op. & print a//b with remainder

a = int(input())
b = int(input())
i = 0
while(a>=b):
    a = a-b
    i += 1
print(i,a)

''' 10/ 2 = 5
10-2 = 8
8-2= 6.......2-2 = 0'''

'''13/ 2
13-2 =11
11-2 = 9...........3-2 = 1(rem)'''