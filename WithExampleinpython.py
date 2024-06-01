# file handling

# 1) without using with statement
file = open('C:\\Users\\shyan\\PycharmProjects\\pythonProjectTest\\config.txt', 'w')
file.write('hello world !')
file.close()

# 2) without using with statement
file = open('C:\\Users\\shyan\\PycharmProjects\\pythonProjectTest\\config.txt', 'w')
try:
	file.write('hello world')
finally:
	file.close()

print("------------------------------------")
# using with statement
with open('C:\\Users\\shyan\\PycharmProjects\\pythonProjectTest\\config.txt', 'w') as file:
	file.write('hello world !')
