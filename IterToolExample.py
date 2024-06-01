import sys

print("the name of the program is ", sys.argv[0])
print("argument list :", sys.argv)

print(list(zip([1, 2, 3,4,5], ['a', 'b', 'c','d'])))

print("the name of the program is ", sys.argv[0])
a = sys.argv[0]
print(a)

print("the name of the program is ", sys.argv[0])

n = len(sys.argv[0])
print("n ",n)
a = sys.argv[0][0:n - 1]
a = a.split(', ')
print("=============")
for i in a:
    print(i)



