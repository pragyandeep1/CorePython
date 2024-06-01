def my_func1():
    global a
    a = 10
    b = 20
    global c
    c = a+b
    print(b)

my_func1()

def func2():
    print(a)
    print(c)
    print(b)

func2()
