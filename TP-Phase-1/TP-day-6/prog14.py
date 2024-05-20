#decorator func
def decorator(func):
    def inner():
        print("hello")
        func()
        print("it will print after x func call")
    return inner
def x():
    print("X func will be printed")
i = decorator(x)
i()