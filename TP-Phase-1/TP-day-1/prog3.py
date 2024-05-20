#take 2 nums from user and multiply them without using * Op.

a = int(input())
b = int(input())
print(int(a/(1/b)))
r = 0
for i in range(b):
    r += a
print(r)