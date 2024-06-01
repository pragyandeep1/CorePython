class Duck:
 def talk(self):
  print('Quack.. Quack..')

class Dog:
 def talk(self):
  print('Bow Bow..')

class Cat:
 def talk(self):
  print('Moew Moew ..')

class Goat:
 def talk(self):
  print('Myaah Myaah ..')
 def f1(obj):
  obj.talk()

class Client:
 l = [Duck(),Cat(),Dog(),Goat()]
 for obj in l:
  obj.talk()