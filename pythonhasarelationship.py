class Engine:
 a = 10
 def __init__(self):
  self.b = 20
  print(self.b)
 def m1(self):
  print('Engine Specific Functionality')

class Car:
 def __init__(self):
  self.engine = Engine()

 def m2(self):
  print('Car using Engine Class Functionality')
  print(self.engine.a)
  print(self.engine.b)
  self.engine.m1()
c = Car()
c.m2()