from corepython.Car import Car


class Employee:
  print("Puneeth")
  def __init__(self,ename,eno,car):
   self.ename=ename
   self.eno=eno
   self.car=car
  def empinfo(self):
   print("Employee Name:",self.ename)
   print("Employee Number:",self.eno)
   print("Employee Car Info:")
   self.car.getinfo()
c=Car("Innova","2.5V","Grey")
e=Employee('Durga',10000,c)
e.empinfo()