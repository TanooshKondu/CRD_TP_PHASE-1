# #exception handling
# try:
#     print(10/1)#print(10/0)--> ZeroError
# except IndexError:
#     print("Divied by zero")
# finally:
#     print("Tanoosh")
    
    
# #############################################3333

# #Raise error 
# raise IndexError("Error Found")
# #function decorators
def fun(s):
    return s.upper()
x= fun
print(x("Tanoosh"))

#################
def upp(s):
    return s.upper()
def sml(s):
    return s.lower()
def name(func, s):
    return func(s)
print(name(upp, "weiuohef"))
print(name(sml, "AIdhncasSO"))
#########################################################
def fun(s1):
    def cont(s2):
        return s1+s2
    return cont
x= fun("abdcddc")
print(x("ubhnuh"))
###
def fun(s1):
    def cont(s2):
        return s1+s2
    return cont
x= fun(23)
print(x(45))