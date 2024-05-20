#infosys Ques

def fun(l):
    try:
        n = len(l)
        o = l[0]//l[n]
    except ZeroDivisionError:
        print("Zero divisin Error")
    except NameError:
        print("Name Error")
    finally:
        print("End of function")
try:
    l=[1,2,3,4,5]
    fun(l)
except IndexError:
    print("Index error")
finally:
    print("end of finally")
    
