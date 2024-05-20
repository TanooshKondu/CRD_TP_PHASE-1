# s1 = input("Enter First Name:  ").strip()
# s2 = input("Enter Second Name:  ").strip()
# # dup = set(s1).intersection(set(s2))
# # print(dup)
# # count = 0
# # for i in s1+s2:
# #     if i not in dup:
# #         count += 1
# # print(count)
# # f = {'F','L','A','M','E','S'}
# # ans=[]
# # for x in range(count):
# #     if count == x:
# #         ans.remove(f[x])
# s1 = list(s1)
# s2 = list(s2)
# for i in range(len(s1)):
#     for j in range(len(s2)):
#         if s1[i] == s2[j]:
#             s1[i] = '0'
#             s2[j] = '0'
#             break
# count = 0
# for i in s1+s2:
#     if i != '0':
#         count += 1
# print(count)
# l = ['f','l','a','m','e','s']
# while(len(l)>1):
#     splitindex = (count%)


import streamlit as st
st.title("Welcome to the game")
s1=st.text_input('Enter first name-')
s2=st.text_input("Enter second name-")
s1=list(s1)
s2=list(s2)
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            s1[i]='0'
            s2[j]='0'
            break
count=0
for i in s1+s2:
    if i!='0':
        count+=1
# 
l=['f','l','a','m','e','s']
while(len(l)>1):
    splitindex=(count%len(l)-1)
    if splitindex >= 0:
        left=l[:splitindex]
        right=l[splitindex+1:]
        l=right+left
    else:
        l= l[:len(l)-1]
if st.button('submit'):
    st.success(l[0])