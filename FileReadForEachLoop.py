f = open("test.txt", 'r', encoding='utf-8')

for line in f:
 print(line, end = '')

print('end of the file execution')
