class Car:
 def __init__(self,name,model,color):
  self.name=name
  self.model=model
  self.color=color
 def getinfo(self):
  print("Car Name:{} , Model:{} and Color:{}".format(self.name,self.model,self.color))