class Test:
 x=10
 _y=20
 __z=30
 def m1(self):
  print(Test.x)
  print(Test._y)
  print(Test.__z)

t=Test()
t.m1()
print(Test.x)
print(Test._y)
print(Test.__z)