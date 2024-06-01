import random
import os
import sys
print(random.random())
print(random.randint(1, 100))
print(random.randrange(1, 10, 1))
print(random.randrange(0, 101, 10))
print(random.choice([12,23,45,67,65,43]))
print('---------------------------')
numbers=[12,23,45,67,65,43]
print("before suffling coll "+numbers.__str__())
random.shuffle(numbers)
print("after suffling coll "+numbers.__str__())
print(numbers)
print("current working directory ",os.getcwd())

print("You entered: ",sys.argv[1], sys.argv[2], sys.argv[3])
