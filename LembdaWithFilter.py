# Python code to illustrate
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

finalist = list(filter(lambda x: (x % 2 == 0), li))
print(finalist)
