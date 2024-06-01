a = 5
print("The type of a", type(a))

b = 40.5
print("The type of b", type(b))

c = 1+3j
print("The type of c", type(c))
print(" c is a complex number", isinstance(1+3j,complex))

print('\n\n\n')

str = "string using double quotes"
print(str)
s = ''''A multiline
string'''+'"""'
print(s)

print('\n\n\n')

str1 = 'hello javatpoint' #string str1
str2 = ' how are you' #string str2
print (str1[0:2]) #printing first two character using slice operator
print (str1[4]) #printing 4th character of the string
print (str1*2) #printing the string twice
print (str1 + str2)

def fun_Generator():
    yield 1
    yield 2
    yield 3

# Driver code to check above generator function
for value in fun_Generator():
    print(value)


def return_none():
    a = 10
    b = 20
    c = a + b
x = return_none()
print(x)
print("\n\n\n")

a = lambda x: x**2
for i in range(1,6):
  print(a(i))
print("\n\n\n")

a = 0
while(a<5):
  print(a)
  a+=1

print("\n\n\n")

list = [1,2,3,4,5]
for i in list:
 print(i)

print("\n\n\n")

a=0
b=5
try:
 c = b/a
 print(c)
except Exception as e:
 print(e)
finally:
 print('Finally always executed')

print("\n\n\n")

a = 5
try:
    if a > 2:
        raise Exception('a should not exceed 2')
except Exception as e:
    print("Exception:", e)

print("\n\n\n")

a = 0
try:
  b = 1/a
except Exception as e:
  print(e)

print("\n\n\n")

a=10
b=12
del a
print(b)
# a is no longer exist
#print(a)

print("\n\n\n")

marks = int(input("Enter the marks:"))
if(marks>=90):
  print("Excellent")
elif(marks<90 and marks>=75):
  print("Very Good")
elif(marks<75 and marks>=60):
  print("Good")
else:
  print("Average")

print("\n\n\n")

n = 11
if(n%2 == 0):
 print("Even")
else:
 print("odd")

print("\n\n\n")

f = open("C://Users/Pragyandeep/Desktop/18-04/corepython/test.txt")

f = open("C://Users/Pragyandeep/Desktop/18-04/corepython/test.txt", mode='r', encoding='utf-8')