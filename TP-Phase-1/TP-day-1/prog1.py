# # print('osijaefwpio    89437509@#',end="         ")
# # print("dsnfsi pfsadg s")
# # print("Hello World")
# # print("sdailfnsa","oiashdfopiseiof","weigofylgweiy","weiuofhupiqehf", sep="   ")
# # print(2 and 3 or 4)
# # a = int(input())
# # b = int(input())
# # print(a+b)
# import random
# a= input()
# b= input()
# print("Love percentage:", random.randint(0,100), end=" %")
n = int(input())
# if n % 4 ==0:
#     if n % 100 == 0 and n % 400 != 0:
#             print("Non - Leap Year")
#     else:
#         print("Leap Year")
# else:
#     print("Non - Leap Year")
if n % 400 == 0 or (n % 100 !=0 and n % 4 == 0):
    print("Leap Year")
else:
    print("Non - Leap Year")